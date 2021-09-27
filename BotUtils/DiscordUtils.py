import os;
import discord;
from discord.ext import commands


def GetLogginToken():
    return os.getenv('DISCORD_TOKEN');

def CreateDiscordClient():
    return commands.Bot(command_prefix= '.');


def ExistTextChannel(DiscordClient , Server):
    return True;


def GetUsersLists( channel):
    return channel.users();


def UserExistOnChannel(channel, user):
    return user in channel.users();


def SendMessage(message):
    return f'```{message}```';

def SendFile(ctx, filePath):
   ctx.send(file = discord.File(filePath));
