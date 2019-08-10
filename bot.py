import discord
from discord.ext import commands
import asyncio
import requests
import os

description = '''EchoBot by Echolandia Studios'''
bot = commands.Bot(command_prefix='-', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("with the API")
    await client.change_presence(status=discord.Status.idle, activity=game)
	
@bot.command()
async def announcement(ctx, *, args):
	"""Announcement command!"""
	embed=discord.Embed(title="Announcement", description=args, color=0x7700aa)
	embed.set_footer(text="By Echolandia Studios")
	await ctx.send("", embed=embed)

bot.run(str(os.environ.get('BOT_TOKEN')))
