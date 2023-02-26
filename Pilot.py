import random
from BotAI import BotAI
from Action import Action
from Action import MoveAction

class Pilot:
    def __init__(self, name):
        self.name = name
        self.bots = []
        self.color = (0, 0, 0) #default black
        self.game = None

    def set_game(self, game):
        self.game = game
    def add_bot(self, bot):
        self.bots.append(bot)
        bot.pilot = self
    def get_action_list(self):
        actions = []
        for bot in self.bots:
            action_list = bot.get_actions()
            selected_actions = self.choose_actions(self.game, bot, action_list)
            actions.extend(selected_actions)

        return actions
    def handle_input(self):
        raise NotImplementedError
    def make_decision(self):
        raise NotImplementedError
    def update(self):
        # Default behavior is to do nothing
        pass
class AiPilot(Pilot):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.bots = []
        self.color = (0, 0, 0)  # default black
        self.bot_ai = BotAI("Brain")
    def handle_input(self):
        # AI Pilots don't need to handle input
        pass
    def add_bot(self, bot):
        self.bots.append(bot)
        bot.pilot = self
    def choose_actions(self, game, bot, action_list):
        selected_actions = self.bot_ai.choose_actions(game, bot, action_list)
        return selected_actions

    def update(self):
        # TODO: Implement any necessary updates to the AI Pilot
        pass

class PlayerPilot(Pilot):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self):
        # TODO: Implement player input handling logic
        pass
    def update(self):
        # TODO: Implement any necessary updates to the player pilot
        pass