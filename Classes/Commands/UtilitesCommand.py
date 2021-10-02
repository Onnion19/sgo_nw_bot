
from Classes.Commands.CommandBaseClass import CommandBase
from Classes.Requests.RequestList import RequestList as Requests
import random
import BotUtils.SystemUtils as S_Utils
import BotUtils.DiscordUtils as D_Utils
import discord
import os

"""
Submodule / Commands for handle the stock. It should: 
"""

class UtilitiesCommand(CommandBase):
    def __init__(self):
        CommandBase.__init__(self)
        self.Requests = Requests()
        self.FileName = "SGO_NW_CraftRequests.csv"
        self.Admins = ["Onnion", "Yirak","NYX トウキﾖウ"]
        self.Requests.InitFromFile(self.FileName)
        S_Utils.CopyFile(self.FileName, self.FileName + ".backup")

    def InitializeModule(self):
        CommandBase.InitializeModule(self)

        @self.CommandBot.command(aliases=['request', 'Request','r'])
        async def AddRequestCommand(ctx, *args):
            if(len(args) < 2):
                await ctx.send(D_Utils.SendMessage("Missing arguments"))
                return
            ammount = args[0]
            if(not ammount.isnumeric()):
                await ctx.send(D_Utils.SendMessage("Incorrect format"))
                return
            item = S_Utils.TupleToString(args[1:],"_")
            self.Requests.AddRequest(item.lower(), ctx.author.name  , int(ammount))
            self.Requests.Serialize(self.FileName)
            await ctx.message.add_reaction('👍')

        @self.CommandBot.command(aliases=['ListRequests','listRequests','listrequests','lr'])
        async def GetAllRequests(ctx, *args):
                if(len(args) > 0):
                    #check if the param to filter is an existing user
                    userName = S_Utils.TupleToString(args)
                    s = self.Requests.SearchUserRequests(userName)
                    if(s != ""):#found user requests
                        s = "Request made by user " + userName + s
                    else:#user was not found as a requester, maybe it's an item
                        s = self.Requests.ItemRequestString(args[0].lower(),"\t")
                    if(s == ""):
                        s = "No user or item found"
                    await ctx.send(D_Utils.SendMessage(s))
                else:
                    await ctx.send(D_Utils.SendMessage(self.Requests.ToString("\t")))


        @self.CommandBot.command(aliases=['backup','BackUp','bu','file'])
        async def GetFile(ctx, *args):
                S_Utils.CopyFile(self.FileName, self.FileName + ".backup")
                await ctx.send(file = discord.File(self.FileName))

        @self.CommandBot.command(aliases=['closeRequest','closerequest', 'cr'])
        async def CloseRequest(ctx, *args):
            if(len(args) < 2):
                await ctx.send(D_Utils.SendMessage("Missing arguments"))
                return

            item = args[0]
            requester = S_Utils.TupleToString(args[1:])
            self.Requests.RemoveRequest(item.lower(), requester)
            self.Requests.Serialize(self.FileName)
            await ctx.message.add_reaction('👍')

        @self.CommandBot.command(aliases=['closeAllRequest','closeallrequest', 'cr_all'])
        async def CloseAllRequest(ctx, *args):
            if(len(args) < 1):
                await ctx.send(D_Utils.SendMessage("Missing user name"))
                return

            requester = S_Utils.TupleToString(args[0:])
            s = self.Requests.RemoveAllUserRequests(requester)
            self.Requests.Serialize(self.FileName)
            await ctx.send(D_Utils.SendMessage("Removed Requests:\n\t"+s))
            await ctx.message.add_reaction('👍')

        @self.CommandBot.command(aliases=['deliverRequest', 'deliverrequest', 'dr'])
        async def DeliverRequest(ctx, *args):
            if(len(args) < 3):
                await ctx.send(D_Utils.SendMessage("Missing arguments"))
                return

            ammount = int(args[0])
            item = args[1]
            requester = S_Utils.TupleToString(args[2:])
            self.Requests.RemoveRequest(item.lower(), requester, ammount)
            self.Requests.Serialize(self.FileName)
            await ctx.message.add_reaction('👍')

        

        @self.CommandBot.command(aliases=['recover', 'rc'])
        async def RecoverFromFile(ctx, *args):
            path = self.FileName
            if(len(args) >= 1):
                if(args[0] == "last"):
                    path +=".tmp"
                else:
                    path = args[0]
            else:
                path += ".backup"

            self.Requests.InitFromFile(path)
            self.Requests.Serialize(self.FileName)
            await ctx.message.add_reaction('👍')

        @self.CommandBot.command(aliases=['clear', 'cl'])
        async def ClearAll(ctx, *args):
            self.Requests.Serialize(self.FileName+".clear")
            if(ctx.author.name in self.Admins):
                self.Requests.WipeData()
                await ctx.message.add_reaction('👍')
            else:
                await ctx.send(D_Utils.SendMessage("You have no permissions"))

        @self.CommandBot.command(aliases=['recoverClear'])
        async def RecoverClearAll(ctx, *args):
            try:
                self.Requests.InitFromFile(self.FileName+".clear");
            except IOError:
                print("Could not the file to load for recover the clear")


        @self.CommandBot.command(aliases=['man', 'ayuda','h'])
        async def DisplayHelp(ctx, *args):
            s = ".request (.r) [ammount] [item] for requesting a item.\n\t Example: .request 150 Arroz con gambas\n\n"
            s += ".listRequest (.lr) [Optional: item/username] see all the requests for all items, or a filtered version if an item or username is specified.\n\t Example: .listRequest or .listRequest Arroz pr .listRequest userName\n\n"
            s += ".deliverRequest (.dr) [ammount] [item] [requester] delivers the ammount if items to the requester.\n\t Example .dr Arroz 60 Onnion\n\n"
            s += ".closeRequest (.cr) [item] [requester]  close a request made for user 'requester'.\n\t Example: .closeRequest Arroz Onnion\n\n"
            s += ".closeAllRequest (.car) [requester] Closes all request made by the requester.\n\t Examepl: .closeAllRequest Onnion\n\n"
            s += ".backup to get a backup file in .csv format.\n\n"
            s += ".recover [last] to recover data as a rollback. By default it recovers from the point when the bot was booted last time. If Last parameter is specified, it will recover from the last command.\n\t Example: .recover or .recover last\n\n"
            s += ".clear wipes all data\n"
            await ctx.send(D_Utils.SendMessage(s))

