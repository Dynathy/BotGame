# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import pygame
from Weapon import Weapon
from Upgrades import Upgrades
from Bot import Bot
from Pilot import AiPilot
from Game import Game

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_TITLE = "Robot Battle Game"


logging.basicConfig(filename='game.log', level=logging.INFO)


def setup_bots():
    # Create the bots
    bot1 = Bot("Bot1", 100, 10, 1, 50, 5, 75, 10, 5, 10, 0, Weapon("laser"), Upgrades("Shield"))
    bot2 = Bot("Bot2", 100, 10, 1, 50, 5, 75, 10, 5, 10, 0, Weapon("laser"), Upgrades("Shield"))

    # Return the bots
    return [bot1, bot2]
def main():
    # Initialize pygame
    pygame.init()

    # Create the game object
    game = Game()

    # Set up some players
    ai_pilot1 = AiPilot("AI Pilot 1")
    ai_pilot2 = AiPilot("AI Pilot 2")

    # Set up some bots
    bots = setup_bots()

    # Assign bots to players
    ai_pilot1.add_bot(bots[0])
    ai_pilot2.add_bot(bots[1])

    # Add players to the game
    game.add_pilot(ai_pilot1)
    game.add_pilot(ai_pilot2)

    # Set Up some bots in the Game
    game.setup_bots(bots)

    #make some visuals
    game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    # Main game loop
    while not game.game_over():
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #game.quit()

        # Handle computer player input
        ai_pilot1.move()
        ai_pilot2.move()

        # Update the game state
        game.update()

        # Render the game
        game.render()

    # Quit pygame
    pygame.quit()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
