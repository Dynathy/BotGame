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
        print(f"Number of Pilots: {len(self.pilots)}")
    def setup_bots(self, bots):
        self.bots = bots
        self.pilots.extend(bot.get_pilot() for bot in bots)
        logging.info(f'Set up {len(self.bots)} bots')
        print(f"Number of Pilots: {len(self.pilots)}")
    def handle_pilot_actions(self):
        # Pass game instance to pilots
        for pilot in self.pilots:
            pilot.set_game(self)

        # Get the action lists for each pilot
        logging.info("Getting action lists...")
        print(f"Number of Pilots: {len(self.pilots)}")
        action_lists = [pilot.get_action_list() for pilot in self.pilots]
        logging.info("Retrieved action list!")
        logging.info("Combining action lists...")
        # Combine all the action lists into a single list and sort them
        actions = []
        for action_list in action_lists:
            actions.extend(action_list)
        actions.sort(key=lambda action: (action.position, action.priority, action.bot.speed, action.bot.max_hp))
        logging.info("Combined action list!")
        logging.info("Executing actions...")
        # Execute the actions using the action handler
        self.action_handler.process_actions(actions)
        logging.info("Actions Executed!")

    def next_turn(self):
        self.turn_counter += 1
    def game_over(self):
        return self.finished
    def update(self):
        for bot in self.bots:
            bot.update()
        for player in self.pilots:
            player.update()
