import random
from Action import Action
from Action import moveAction

class Pilot:
    def __init__(self, name):
        self.name = name
        self.bots = []
        self.color = (0, 0, 0) #default black

    def set_game(self, game):
        self.game = game
    def add_bot(self, bot):
        self.bots.append(bot)
        bot.pilot = self
    def handle_input(self):
        raise NotImplementedError

    def make_decision(self):
        raise NotImplementedError
    def update(self):
        # Default behavior is to do nothing
        pass
class AiPilot:
    def __init__(self, name):
        self.name = name
        self.bots = []
        self.color = (0, 0, 0)  # default black
    def handle_input(self):
        # AI Pilots don't need to handle input
        pass
    def add_bot(self, bot):
        self.bots.append(bot)
        bot.pilot = self
    def move(self):
        # TODO: Implement AI logic to determine bot movement
        pass

    def update(self):
        # TODO: Implement any necessary updates to the AI Pilot
        pass

class PlayerPilot(Pilot):
    def __init__(self, bot):
        super().__init__(bot)

    def handle_input(self):
        # TODO: Implement player input handling logic
        pass
    def update(self):
        # TODO: Implement any necessary updates to the player pilot
        pass