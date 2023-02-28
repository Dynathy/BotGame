import logging
import math
import pygame
from StatusEffect import StatusEffect

class Bot:
    def __init__(self, name, point_value, max_ap, ap_regen, max_hp, speed, accuracy, evasion, defense, armor, shielding, weapons, upgrades):
        self.name = name
        self.point_value = point_value
        self.max_ap = max_ap
        self.ap_regen = ap_regen
        self.ap = max_ap
        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.accuracy = accuracy
        self.evasion = evasion
        self.defense = defense
        self.armor = armor
        self.shielding = shielding
        self.weapons = []
        self.upgrades = []
        self.weapons.append(weapons)
        self.upgrades.append(upgrades)
        self.damage = 0
        self.pos_x = 0
        self.pos_y = 0
        self.pilot = None
        self.status_effects = []
        self.actions = {
            'move': {'enabled': True, 'ap_cost': 1},
            'attack': {'enabled': True, 'ap_cost': 1},
            'defend': {'enabled': True, 'ap_cost': 2},
        }

        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Name: {self.name}, Point Value: {self.point_value}, Max AP: {self.max_ap}, AP Regen: {self.ap_regen}")
        self.logger.info(f"AP: {self.ap}, Max HP: {self.max_hp}, HP: {self.hp}, Speed: {self.speed}")
        self.logger.info(f"accuracy: {self.accuracy}, evasion: {self.evasion}, defense: {self.defense}, armor: {self.armor}")
        self.logger.info(f"Shielding: {self.shielding}")
    def set_actions(self, name, value):
        if name in self.actions:
            self.actions[name] = value
            self.logger.info(f"{self.name} {name} set to {value}")
        else:
            self.logger.warning(f"Action {name} does not exist for {self.name}")
    def decrement_status_effects(self):
        effects_to_remove = []
        for effect in self.status_effects:
            effect.duration -= 1
            if effect.duration == 0:
                effects_to_remove.append(effect)

        for effect in effects_to_remove:
            self.status_effects.remove(effect)
    def get_action_ap_cost(self, action_name):
        if action_name in self.actions:
            return self.actions[action_name]["ap_cost"]
        else:
            return 0
    def get_actions(self):
        return [action for action, data in self.actions.items() if data['enabled'] and data['ap_cost'] <= self.ap]
    def get_pilot(self):
        return self.pilot
    def update(self):
        self.logger.warning(f"The Update method is not implemented")

    def calculate_status_effect(self):
        # Get a copy of the bot's attributes and actions
        bot_attributes = {
            'max_ap': self.max_ap,
            'ap_regen': self.ap_regen,
            'max_hp': self.max_hp,
            'speed': self.speed,
            'accuracy': self.accuracy,
            'evasion': self.evasion,
            'defense': self.defense,
            'armor': self.armor,
            'shielding': self.shielding,
        }

        bot_actions = {action: data.copy() for action, data in self.actions.items()}
        status_effects = self.status_effects
        # Add together the changes from each status effect
        for effect in status_effects:
            for attribute, value in effect.get_attributes_dict().items():
                if attribute in bot_attributes:
                    bot_attributes[attribute] += value

            for action, data in effect.get_actions_dict().items():
                if action in bot_actions:
                    bot_actions[action]['enabled'] = bot_actions[action]['enabled']

        self.logger.info(f"{self.name}'s status attributes: {bot_attributes}")
        self.logger.info(f"{self.name}'s status actions: {bot_actions}")

        return {
            'attributes': bot_attributes,
            'actions': bot_actions,
        }
    def move(self, direction):
        # Determine angle to move in based on the cardinal direction
        angle_map = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}
        angle = angle_map[direction]

        # Get a copy of the bots Attributes and Actions after Status Effect Mods
        status_effect = self.calculate_status_effect()

        # Check to see if Move is still enabled (Potentially disabled due to status effect)
        move_enabled = status_effect['actions']['move']['enabled']
        if move_enabled:
            # Get the wiggle room from the BotAI
            bot_ai = self.get_pilot().bot_ai
            wiggle_room = bot_ai.get_wiggle_room()

            # Modify the angle by the wiggle room and move the bot
            angle += wiggle_room
            radians = math.radians(angle)
            x_delta = (self.speed * 10) * math.cos(radians)
            y_delta = (self.speed * 10) * math.sin(radians)
            prev_x, prev_y = self.pos_x, self.pos_y
            self.pos_x += x_delta
            self.pos_y += y_delta
            self.logger.info(f"Moved {direction} with wiggle room of {wiggle_room}")

            # Check for collision with boundaries
            if self.pos_x < 0:
                self.pos_x = 0
            elif self.pos_x > pygame.display.get_surface().get_width():
                self.pos_x = pygame.display.get_surface().get_width()
            if self.pos_y < 0:
                self.pos_y = 0
            elif self.pos_y > pygame.display.get_surface().get_height():
                self.pos_y = pygame.display.get_surface().get_height()

            # Check for collision with other bots
            for bot in self.get_pilot().game.bots:
                if bot != self and abs(bot.pos_x - self.pos_x) < 10 and abs(
                        bot.pos_y - self.pos_y) < 10:
                    self.pos_x, self.pos_y = prev_x, prev_y
                    bot.pos_x, bot.pos_y = bot.prev_x, bot.prev_y
                    self.logger.info(f"Collision detected with bot {bot.bot_id}.")



            # Increase Evasion by the bots Speed stat
            new_effect = StatusEffect("Evasion +", 1, self.actions)
            new_effect.modify_attribute('evasion', self.speed)
            self.status_effects.append(new_effect)
        # If Move was disabled, the bot will cancel the action and refund the AP
        else:
            self.logger.info("Bot Cancelled Action")
            move_ap_cost = status_effect['actions']['move']['ap_cost']
            self.ap += move_ap_cost
            self.logger.info(f"Refunded {move_ap_cost} AP for Move action")

    def attack(self, target, weapon):
        self.logger.warning(f"The ATTACK action is not implemented")
    def defend(self):
        self.logger.warning(f"The DEFEND action is not implemented")
