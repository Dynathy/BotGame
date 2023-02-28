class StatusEffect:
    def __init__(self, name, duration, actions):
        self.name = name
        self.duration = duration
        self.actions = actions
        self.attributes = {
            'max_hp': 0,
            'hp': 0,
            'max_ap': 0,
            'ap': 0,
            'strength': 0,
            'defense': 0,
            'speed': 0,
            'evasion': 0,
            'accuracy': 0,
            'luck': 0
        }
    def modify_attribute(self, key, value):
        self.attributes[key] = value

    def modify_action(self, key, enabled=None, ap_cost=None):
        if key not in self.actions:
            self.actions[key] = {'enabled': True, 'ap_cost': 0}
        if enabled is not None:
            self.actions[key]['enabled'] = enabled
        if ap_cost is not None:
            self.actions[key]['ap_cost'] = ap_cost
    def decrement_duration(self):
        self.duration -= 1
    def get_attributes_dict(self):
        return self.attributes.copy()

    def get_actions_dict(self):
        return self.actions.copy()