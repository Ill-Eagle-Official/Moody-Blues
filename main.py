import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    print("Message received: ", message.content)
    print("Channel: ", message.channel)
    if message.content.startswith == "!move":
        print("message sent")
        try:
            await message.channel.send("Moving out!")
        except Exception as e:
            print("Error: ", e)


client.run("MTA1OTU4MzUxMzQ5OTc5NTQ2Ng.GJIR3D.bzGNxI0iOblfjg-xURAXa3-yh_wtj-LpuHKZSw")
