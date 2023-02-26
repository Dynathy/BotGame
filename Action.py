class Action:
    def __init__(self, bot, position, priority):
        self.bot = bot
        self.position = position
        self.priority = priority
    def __str__(self):
        return f"{self.__class__.__name__} - Bot: {self.bot.id}, Position: {self.position}, Priority: {self.priority}"
    def execute(self):
        pass

class DefendAction(Action):
    def __init__(self, bot, position, priority):
        super().__init__(bot, position, priority)

    def execute(self):
        self.bot.defend()
class MoveAction(Action):
    def __init__(self, bot, position, priority, direction):
        super().__init__(bot, position, priority)
        self.direction = direction

    def execute(self):
        self.bot.move(self.direction)

class AttackAction(Action):
    def __init__(self, bot, position, priority, target, weapon):
        super().__init__(bot, position, priority)
        self.target = target
        self.weapon = weapon

    def execute(self):
        self.bot.attack(self.target, self.weapon)

