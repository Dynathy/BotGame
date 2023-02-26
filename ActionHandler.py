import logging
class ActionHandler:
    def process_actions(self, action_list):
        for action in action_list:
            if hasattr(action, 'execute') and callable(action.execute):
                action.execute()
            else:
                logging.warning(f"Action {action} does not have an execute method")

