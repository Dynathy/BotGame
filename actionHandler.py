class actionHandler:
    def __init__(self, players):
        self.players = players
        self.actions = []

    def handle_actions(self):
        for player in self.players:
            actions = player.make_actionList()
            self.actions += actions
        self.actions.sort(key=lambda action: (action.position, action.priority, action.bot.speed, action.bot.max_hp))

        return self.actions

    def process_actions(self, action_list):
        for action in action_list:
            action.execute()

    def clear_action_lists(self):
        self.actions = []
