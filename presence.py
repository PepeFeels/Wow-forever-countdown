
import os
import discord

TOKEN = os.environ["DISCORD_BOT_TOKEN"]

intents = discord.Intents.none()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Online som {client.user}", flush=True)
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name="WoW Forever Countdown"),
    )


client.run(TOKEN)
