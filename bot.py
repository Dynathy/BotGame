import math
import random
class bot:
    def __init__(self, name, point_value, max_ap, ap_regen, ap, max_hp, speed, accuracy, evasion, defense, armor, shielding, weapons, upgrades):
        self.name = name
        self.point_value = point_value
        self.max_ap = max_ap
        self.ap_regen = ap_regen
        self.ap = ap
        self.max_hp = max_hp
        self.speed = speed
        self.accuracy = accuracy
        self.evasion = evasion
        self.defense = defense
        self.armor = armor
        self.shielding = shielding
        self.weapons = weapons
        self.upgrades = upgrades

        self.damage = 0
        self.pos_x = 0
        self.pos_y = 0

    def attack(self, target, weapon):
        print("attacks target")


    def move(self, angle):
        distance = self.speed * 10
        wiggle_room = angle / 4
        angle += random.uniform(-wiggle_room, wiggle_room)
        self.pos_x += distance * math.cos(angle)
        self.pos_y += distance * math.sin(angle)
        if self.pos_x < 0:
            self.pos_x = 0
        if self.pos_x > 800:
            self.pos_x = 800
        if self.pos_y < 0:
            self.pos_y = 0
        if self.pos_y > 600:
            self.pos_y = 600

    def setup(self, x, y):
        self.pos_x = x
        self.pos_y = y

