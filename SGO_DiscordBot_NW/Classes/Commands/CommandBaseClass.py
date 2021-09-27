


class CommandBase:

    def __init__(self):
        self.CommandBot = None;


    def SetBotCommand(self, InCommandBot):
        self.CommandBot = InCommandBot;

    def InitializeModule(self):
        pass
