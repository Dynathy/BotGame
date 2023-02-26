import logging
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
    def move(self, direction):
        self.logger.warning(f"The MOVE action is not implemented")
    def attack(self, target, weapon):
        self.logger.warning(f"The ATTACK action is not implemented")
    def defend(self):
        self.logger.warning(f"The DEFEND action is not implemented")