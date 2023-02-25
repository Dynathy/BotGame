import pygame.display

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_TITLE = "Robot Battle Game"
class Renderer:
    def __init__(self, game, pygame):
        self.game = game
        self.pygame = pygame
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background_color = (255, 255, 255)  # white

    def render(self, game):
        self.screen.fill(self.background_color)

        for bot in self.game.bots:
            pilot_color = bot.pilot.color
            bot_pos_x = bot.pos_x
            bot_pos_y = bot.pos_y
            pygame.draw.circle(self.screen, pilot_color, (bot_pos_x, bot_pos_y), 10)

        pygame.display.flip()

