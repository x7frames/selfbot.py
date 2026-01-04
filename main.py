import discord

from discord.ext import commands

bot commands.Bot(command_prefix="1", intentsadiscord.Intents.all(), self_botaTrue)



@bot.event

async def on_ready():

print(f'(bot.user.name) is now online')



@bot.command()

async def ping(ctx):

await ctx.send('pong")

bot.run("your token here")
