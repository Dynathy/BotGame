# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import pygame
import sys
from actionHandler import actionHandler
from player import player

logging.basicConfig(filename='game.log', level=logging.INFO)
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mech Battle Simulator")

    #initiate players
    playerOne = player("playerOne")
    playerOne.create_bot()
    playerTwo = player("playerTwo")
    playerTwo.create_bot()
    #set up bots
    for starting_bot in playerOne.get_bots():
        starting_bot.setup(20, 300)

    for starting_bot in playerTwo.get_bots():
        starting_bot.setup(780, 300)

    #setup action handler
    player_list = [playerOne, playerTwo]
    handler = actionHandler(player_list)

    #Game Loop
    while True:
        #test movement


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    action_list = handler.handle_actions()
                    handler.process_actions(action_list)
                    handler.clear_action_lists()
                    playerOne.regen_bots()
                    playerTwo.regen_bots()
                    logging.info(f"End of Turn")

        screen.fill((255, 255, 255))
        for update_bot in playerOne.get_bots():
            pygame.draw.circle(screen, (0, 0, 255), (update_bot.pos_x, update_bot.pos_y), 10)

        for update_bot in playerTwo.get_bots():
            pygame.draw.circle(screen, (255, 0, 0), (update_bot.pos_x, update_bot.pos_y), 10)

        pygame.display.update()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
