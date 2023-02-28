# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import logging
import pygame
import time
from Weapon import Weapon
from Upgrades import Upgrades
from Bot import Bot
from Pilot import AiPilot
from Game import Game
from Renderer import Renderer

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_TITLE = "Robot Battle Game"
MAX_HANDLE_PILOT_ACTIONS_FREQ = 1.0 # in seconds

logging.basicConfig(filename='game.log', level=logging.INFO)


def setup_bots():
    # Create the bots
    logging.info("Creating Bot 1")
    bot1 = Bot("Bot1", 100, 3, 1, 50, 5, 75, 10, 5, 10, 0, Weapon("laser"), Upgrades("Shield"))
    logging.info("Bot 1 Created!")

    logging.info("Creating Bot 2")
    bot2 = Bot("Bot2", 100, 3, 1, 50, 5, 75, 10, 5, 10, 0, Weapon("laser"), Upgrades("Shield"))
    logging.info("Bot 2 Created!")

    logging.info("Placing Bot 1")
    bot1.pos_x = 30
    bot1.pos_y = 300
    logging.info("Bot 1 placed!")

    logging.info("Placing Bot 2")
    bot2.pos_x = 770
    bot2.pos_y = 300
    logging.info("Bot 2 placed!")
    # Return the bots
    return [bot1, bot2]
def main():
    # Initialize pygame
    logging.info("Initializing Pygame...")
    pygame.init()
    logging.info("Pygame Initialized!")

    # Create the game object
    logging.info("Initializing Game...")
    game = Game()
    logging.info("Game Object Created!")

    # Set up some players
    logging.info("Creating Player 1...")
    ai_pilot1 = AiPilot("AI Pilot 1")
    ai_pilot1.color = (255, 0, 0) # red
    logging.info("Player 1 created!")

    logging.info("Creating Player 2...")
    ai_pilot2 = AiPilot("AI Pilot 2")
    ai_pilot2.color = (0, 0, 255)  # red
    logging.info("Player 2 created!")

    # Set up some bots
    logging.info("Setting up Bots...")
    bots = setup_bots()
    logging.info("Bots set up!")

    # Assign bots to players
    logging.info("Assigning bots to players...")
    ai_pilot1.add_bot(bots[0])
    ai_pilot2.add_bot(bots[1])
    logging.info("Bots Assigned!")

    # Add players to the game
    logging.info("Adding players to game...")
    #game.add_pilot(ai_pilot1)
    #game.add_pilot(ai_pilot2)
    logging.info("Players Added!")

    # Set Up some bots in the Game
    logging.info("Placing Bots on the battlefield...")
    game.setup_bots(bots)
    logging.info("Bots placed on battlefield!")

    #make some visuals
    logging.info("Opening Battle feed...")
    renderer = Renderer(game, pygame)
    clock = pygame.time.Clock()
    logging.info("Battle feed Online!")

    # Main game loop
    last_handle_pilot_actions_time = time.time()
    while not game.game_over():
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("Closing Battle Simulator...")
                game.finished = True
                logging.info("Battle Simulator Closed!")
        clock.tick(60)


        if not game.finished:
            # limit the frequency of handle_pilot_actions
            current_time = time.time()
            if current_time - last_handle_pilot_actions_time >= MAX_HANDLE_PILOT_ACTIONS_FREQ:
                last_handle_pilot_actions_time = current_time
                # Handle computer/player action
                game.handle_pilot_actions()

                # Update the game state
                game.update()

                # Progress the Turn
                game.next_turn()

        # Render the game
        renderer.render()

         # Limit frame rate to X FPS

    # Quit pygame
    logging.info("Exiting Pygame...")
    pygame.quit()
    logging.info("Exited Pygame!")
    logging.info("Good Bye!")
    sys.exit()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
