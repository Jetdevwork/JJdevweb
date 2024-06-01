# Import required dependencies
import discord
from discord.ext import commands
from discord import Intents

# Import Bot Token
from apikeys import *

intents = Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready():
    print("Judge is here!")
    print("------------------")

@client.command
async def hello(ctx):
    await ctx.send("Ready to serve")

@client.command
async def hello(ctx):
    await ctx.send("Goodbye")

@client.event
async def on_member_join():
    await member.send("Test")


client.run(BOTTOKEN)
