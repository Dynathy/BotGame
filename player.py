
import math
import random
import logging
from bot import bot
from action import attackAction
from action import moveAction
from weapon import weapon
from upgrades import upgrades

logging.basicConfig(filename='game.log', level=logging.INFO)
class player:

    def __init__(self, name):
        self.name = name
        self.bots = []

    def create_bot(self):
        # create weapons
        bot_gun = weapon("gun")

        # create upgrades
        bot_upgrade = upgrades("upgrade")

        # create bots
        playerBot = bot(self.name, 30, 3, 1, 3, 150, 5, 70, 10, 15, 10, 10, bot_gun, bot_upgrade)

        self.bots.append(playerBot)

    def get_bots(self):
        return self.bots

    def regen_bots(self):
        for bot in self.bots:
            bot.regenAP()

    def make_actionList(self):
        # Direction of movement for later
        DIRECTIONS = {
            "N": 0,
            "NE": 0.25 * math.pi,
            "E": 0.5 * math.pi,
            "SE": 0.75 * math.pi,
            "S": math.pi,
            "SW": 1.24 * math.pi,
            "W": 1.5 * math.pi,
            "NW": 1.75 * math.pi
        }
        action_handler = []

        for bot in self.bots:
            bot_action_list = []
            available_ap = bot.ap

            if available_ap > 0:
                actions = random.randint(0, available_ap)
            else:
                actions = 0

            for i in range(actions):
                moveORattack = random.randint(0, 1)
                if moveORattack == 0: #move
                    random_direction = random.choice(list(DIRECTIONS.keys()))
                    direction = DIRECTIONS[random_direction]
                    bot_action_list.append(moveAction(bot=bot, position=i, priority=1, direction=direction))
                    logging.info(f"{self.name} orders {bot.name} to move {random_direction}. Available AP: {bot.ap}.")
                if moveORattack == 1: #attack
                    bot_action_list.append(attackAction(bot=bot, position=i, priority=2, target=bot, weapon=bot.weapons))
                    logging.info(f"{self.name} orders {bot.name} to attack {bot.name}. Available AP: {bot.ap}.")

                bot_action_list.sort(key=lambda action: (action.position, action.priority, action.bot.speed, action.bot.max_hp))
                action_handler += bot_action_list

        action_handler.sort(key=lambda action: (action.position, action.priority, action.bot.speed, action.bot.max_hp))
        return action_handler
