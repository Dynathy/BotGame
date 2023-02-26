import random
import logging
from Action import MoveAction, AttackAction, DefendAction

ACTION_CLASSES = {
    "defend": DefendAction,
    "move": MoveAction,
    "attack": AttackAction

    # Add more action classes here
}

class BotAI:
    def __init__(self, name):
        self.name = name

    def choose_actions(self, game, bot, action_list):
        logging.info("Bot {} AI is at choose_actions".format(self.name))
        selected_actions = []
        ap = bot.ap
        ap_to_use = random.randint(1, ap)
        logging.info("Bot {} is using {} AP out of {} AP available".format(self.name, ap_to_use, ap))

        while ap_to_use > 0 and action_list:
            valid_actions = [action for action in action_list if bot.get_action_ap_cost(action) <= ap_to_use]

            if valid_actions:
                action_name = random.choice(valid_actions)
                position = len(selected_actions)
                if action_name == "defend":
                    action = self.add_defend_action_details(bot, action_name, position)
                elif action_name == "move":
                    action = self.add_move_action_details(bot, action_name, position)
                elif action_name == "attack":
                    action = self.add_attack_action_details(game, bot, action_name, position)

                selected_actions.append(action)
                ap_to_use -= bot.get_action_ap_cost(action_name)
                ap -= bot.get_action_ap_cost(action_name)
                logging.info("Bot {} is choosing action {} with cost {} AP".format(self.name, action_name, bot.get_action_ap_cost(action_name)))
                logging.info("Bot {} has {} AP left after choosing action {}".format(self.name, ap_to_use, action_name))
            else:
                break
        logging.info("Bot {} has chosen actions {}".format(self.name, selected_actions))
        logging.info("Bot {} has {} AP left after choosing actions".format(self.name, ap))
        return selected_actions

    def add_defend_action_details(self, bot, action_name, position):
        action_class = ACTION_CLASSES[action_name]
        action = action_class(bot, position, 1)
        return action

    def add_move_action_details(self, bot, action_name, position):
        direction = random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
        action_class = ACTION_CLASSES[action_name]
        action = action_class(bot, position, 1, direction)
        return action
    def add_attack_action_details(self, game, bot, action_name, position):
        # Here, you could use the bot's intelligence to determine the best target and weapon to use
        target = random.choice(game.bots)
        weapon = random.choice(bot.weapons)
        action_class = ACTION_CLASSES[action_name]
        action = action_class(bot, position, 1, target, weapon)
        return action
