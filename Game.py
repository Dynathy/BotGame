import logging
class Game:
    def __init__(self):
        self.bots = []
        self.players = []
        self.turn_counter = 0
        self.finished = False

    def add_pilot(self, pilot):
        self.players.append(pilot)
    def setup_bots(self, bots):
        self.bots = bots
        self.players.extend(bot.get_pilot() for bot in bots)
        logging.info(f'Set up {len(self.bots)} bots')
    def next_turn(self):
        self.turn_counter += 1

    def game_over(self):
        return self.finished
    def update(self):
        for bot in self.bots:
            bot.update()
        for player in self.players:
            player.update()

    def render(self):
        #TODO: Implement Render Logic
        pass

    def quit(self):
        #TODO: Implement Quit
        pass