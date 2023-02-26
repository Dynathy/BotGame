import logging
from ActionHandler import ActionHandler
class Game:
    def __init__(self):
        self.bots = []
        self.pilots = []
        self.action_handler = ActionHandler()
        self.turn_counter = 0
        self.finished = False

    def add_pilot(self, pilot):
        self.pilots.append(pilot)
    def setup_bots(self, bots):
        self.bots = bots
        self.pilots.extend(bot.get_pilot() for bot in bots)
        logging.info(f'Set up {len(self.bots)} bots')
    def handle_pilot_actions(self):
        # Pass game instance to pilots
        for pilot in self.pilots:
            pilot.set_game(self)

        # Get the action lists for each pilot
        logging.info("Getting action lists...")
        action_lists = [pilot.get_action_list() for pilot in self.pilots]

        # Combine all the action lists into a single list and sort them
        actions = []
        for action_list in action_lists:
            actions.extend(action_list)
        actions.sort(key=lambda action: (action.position, action.priority, action.bot.speed, action.bot.max_hp))

        # Execute the actions using the action handler
        self.action_handler.process_actions(actions)

    def next_turn(self):
        self.turn_counter += 1
    def game_over(self):
        return self.finished
    def update(self):
        for bot in self.bots:
            bot.update()
        for player in self.pilots:
            player.update()
