import discord
from discord.ext import commands
import asyncio
import requests
import os

description = '''EchoBot by Echolandia Studios'''
bot = commands.Bot(command_prefix='-', description=description)

@bot.event
async def on_ready():
    print('Ready!')
	
@bot.command()
async def announcement(ctx, *, args):
	"""Announcement command!"""
	embed=discord.Embed(title="Announcement", description=args, color=0x7700aa)
	embed.set_footer(text="By Echolandia Studios")
	await ctx.send("", embed=embed)

bot.run(str(os.environ.get('BOT_TOKEN')))
