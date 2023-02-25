class Action:
    def __init__(self, bot, position, priority):
        self.bot = bot
        self.position = position
        self.priority = priority

    def execute(self):
        pass
class moveAction(Action):
    def __init__(self, bot, position, priority, direction):
        super().__init__(bot, position, priority)
        self.direction = direction

    def execute(self):
        self.bot.move(self.direction)

class attackAction(Action):
    def __init__(self, bot, position, priority, target, weapon):
        super().__init__(bot, position, priority)
        self.target = target
        self.weapon = weapon

    def execute(self):
        self.bot.attack(self.target, self.weapon)
