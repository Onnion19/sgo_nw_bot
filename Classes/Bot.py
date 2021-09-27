import os
import discord
import BotUtils.DiscordUtils as d_utils
import BotUtils.SystemUtils as s_utils
from discord.ext import commands
from dotenv import load_dotenv
import random

from BotUtils import DelegatesList



"""
Bot class which is structured of: 
 - List of submodules that wants to answer discord events. (For example one module would be a random nubmer generator, another would be rock scissors paper game, etc).
    - The bot will automatically bind all the submodules callbacks to the discord events. @see Bind_OnXXXX() functions

"""
class SuperDuperBot:

 #----------- BOT EVENT CALLBACKS -------------
    def DefaultOnreadyCallback(self):
        s_utils.SysPrint("SuperDuperBot is ready to go!", s_utils.PrintDecorators.WARNING)
        self.bIsConnected = True #Discord confirms we have established connection.

    def DefaultOnMessageCallback(self, message):
        print(f'{message.author} Sends a new message: {message.content}')

    def __init__(self):
        self.DiscordClient = None
        self.bIsConnected = False
        self.OnReadyHandler = DelegatesList.DelegateList()
        self.OnMessageHandler = DelegatesList.DelegateList()

    def Init(self):
        load_dotenv()

        self.DiscordClient = d_utils.CreateDiscordClient() #Creates a discord connection, and requests to connect to the servers (Not
                                                           #connected yet).
        self.bIsConnected = False

# ------------ DISCORD CONNECTION GETTER---------------
    def GetCommandManager(self):
        return self.DiscordClient

# --------------- BINDINGS ------------
    def Bind_OnReady(self):
        @self.DiscordClient.event
        async def on_ready():
            self.DefaultOnreadyCallback()
            self.OnReadyHandler.Execute()

    def Bind_OnMessage(self):
        @self.DiscordClient.event
        async def on_message(message):

            if(message.author.name == "SGO_NW_Bot"): #Don't answer to himself.
                return

            self.DefaultOnMessageCallback(message)
            self.OnMessageHandler.Execute(message = message)
            await self.DiscordClient.process_commands(message)

    def BindAll(self):
        self.Bind_OnMessage()
        self.Bind_OnReady()

# --------------- MAIN LOOP ---------------
    def RunBot(self):
        self.DiscordClient.run(d_utils.GetLogginToken())

    def bIsClientConnected(self):
        return self.bIsConnected;
