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
    game = discord.Game("with the API")
    await client.change_presence(status=discord.Status.idle, activity=game)
	
@bot.command()
async def announcement(ctx, *, args):
	"""Announcement command!"""
	embed=discord.Embed(title="Announcement", description=args, color=0x7700aa)
	embed.set_footer(text="By Echolandia Studios")
	await ctx.send("", embed=embed)
	
@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

bot.run(str(os.environ.get('BOT_TOKEN')))
