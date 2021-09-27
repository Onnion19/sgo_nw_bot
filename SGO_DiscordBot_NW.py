from Classes.Bot import SuperDuperBot
from Classes.Commands.UtilitesCommand import  UtilitiesCommand
"""
Bot Handler, adds a level of abstraction to the bot

The Handler will create a new bot instance, and perform the setup operations by order: 
    - Initialize the discord connection.
    - Bind all the bot callbacks and delegates to respon discord events.
    - Initialize all the submodules + add the bindings to the discord events.
    - Execute the bot and try to establish connection with discord.
"""
class BotManager:

    def __init__(self):
        self.SDBot = SuperDuperBot();
        self.ModuleList = [UtilitiesCommand()];
        self.SDBot.Init();
        self.SDBot.BindAll();
        self.InitializeModules();
        self.SDBot.RunBot();


    def GetSuperDuperBot(self):
        return self.SDBot.GetCommandManager();

    def AddModule(self, newModule):
        self.ModuleList.append(newModule);

    def InitializeModules(self):
        self.InitializeCommandModules();

    def InitializeCommandModules(self):
        for module in self.ModuleList:
            module.SetBotCommand(self.GetSuperDuperBot());
            module.InitializeModule();


#ENTRY POINT
Manager = BotManager();
