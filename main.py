import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event

async def on_message(message):
    if message.content == '!move':
      await message.channel.send('Moving to the next channel')

client.run('MTA1OTU4MzUxMzQ5OTc5NTQ2Ng.GJIR3D.bzGNxI0iOblfjg-xURAXa3-yh_wtj-LpuHKZSw')