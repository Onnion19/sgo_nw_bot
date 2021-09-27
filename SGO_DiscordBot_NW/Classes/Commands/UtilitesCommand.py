
from Classes.Commands.CommandBaseClass import CommandBase
from Classes.Requests.RequestList import RequestList as Requests
import random
import BotUtils.SystemUtils as S_Utils
import BotUtils.DiscordUtils as D_Utils
import discord

"""
Submodule / Commands for handle the stock. It should: 
"""

class UtilitiesCommand(CommandBase):
    def __init__(self):
        CommandBase.__init__(self)
        self.Requests = Requests()
        self.FileName = "SGO_NW_CraftRequests.csv"

    def InitializeModule(self):
        CommandBase.InitializeModule(self)

        @self.CommandBot.command(aliases=['request', 'Request','r'])
        async def AddRequestCommand(ctx, item, ammount):
            if(not ammount.isnumeric()):
                S_Utils.sysPrint("Incorrect ammount")
                return
            self.Requests.AddRequest(item.lower(), ctx.author.name  , int(ammount))
            self.Requests.Serialize(self.FileName)
            await ctx.message.add_reaction('👍')
            await ctx.send(D_Utils.SendMessage(ctx.author.name));

        @self.CommandBot.command(aliases=['ListRequests','listRequests','listrequests','lr'])
        async def GetAllRequests(ctx, *args):
                if(len(args) > 0):
                    s = self.Requests.ItemRequestString(args[0].lower(),"\t")
                    if(s == ""):
                        s+= "Hurrah! there are no more requests for: " + args[0]
                    await ctx.send(D_Utils.SendMessage(s))
                else:
                    await ctx.send(D_Utils.SendMessage(self.Requests.ToString("\t")))


        @self.CommandBot.command(aliases=['backup','BackUp','bu','file'])
        async def GetFile(ctx, *args):
                await ctx.send(file = discord.File(self.FileName));

        @self.CommandBot.command(aliases=['CloseRequest', 'closeRequest','closerequest', 'cr'])
        async def CloseRequests(ctx, item, requester, ammount=999999):
            if(ammount < 0):
                return

            self.Requests.RemoveRequest(item.lower(), requester, ammount)
            self.Requests.Serialize(self.FileName)
            await ctx.message.add_reaction('👍')

        @self.CommandBot.command(aliases=['man', 'ayuda','h'])
        async def DisplayHelp(ctx, *args):
            s = ".request [item] [ammount] for requesting a item.\n\t Example: .request Arroz 150\n\n"
            s += ".listRequest [Optional: item] see all the requests for all items, or a filtered version if an item is specified.\n\t Example: .listRequest or .listRequest Arroz\n\n"
            s += ".closeRequest [item] [requester] [Optional: ammount] close a request made for user 'requester', provide an ammount if only part of the request has been satisfied.\n\t Example: .closeRequest Arroz Onnion or .closeRequest Arroz Onnion 5\n\n"
            s += ".backup to get a backup file in .csv format."
            await ctx.send(D_Utils.SendMessage(s))

