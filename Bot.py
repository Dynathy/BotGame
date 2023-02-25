
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
        self.weapons = weapons or []
        self.upgrades = upgrades or []
        self.damage = 0
        self.pos_x = 0
        self.pos_y = 0

        self.pilot = None
    def setup(self, x, y):
        # TODO: Implement bot setup logic
        pass
    def execute_action(self, action):
        # TODO: Implement bot action execution logic
        pass

    def get_pilot(self):
        return self.pilot

    def update(self):
        #TODO: Implement Update logic
        pass