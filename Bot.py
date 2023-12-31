import os
import discord
import requests
from PIL import Image
from io import BytesIO
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

BALLS_FOLDER= './Balls'

@bot.event
async def on_ready():
    print(f'{bot.user.name} Is Online ================ ')
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="With Balls"))

@bot.event
async def on_message(message):
    if message.channel.id == 1176568431018004540 and message.attachments:
        attachment = message.attachments[0]
        if attachment.content_type.startswith("image/"):
            await attachment.save("Temp.jpg")

            try:
                with Image.open("Temp.jpg") as sent_image:
                    for filename in os.listdir(BALLS_FOLDER):
                        with Image.open(os.path.join(BALLS_FOLDER, filename)) as reference_image:
                            if sent_image.size == reference_image.size and sent_image.tobytes() == reference_image.tobytes():
                                filename_without_ext = os.path.splitext(filename)[0].split(".")[-1]
                                await message.channel.send(f"Match Found : {filename_without_ext}")

                                os.remove("Temp.jpg")
                                return

                await message.channel.send("No Match Found")

            except Exception as e:

                print(f"Error: {e}")

                await message.channel.send("An Error Occured Processing The Image")
                os.remove("Temp.jpg")


    elif message.author.id == 999736048596816014 and message.content.startswith('A wild countryball appeared!') and message.attachments:
        attachment = message.attachments[0]
        if attachment.content_type.startswith("image/"):
            await attachment.save("Temp.jpg")

            try:
                with Image.open("Temp.jpg") as sent_image:
                    for filename in os.listdir(BALLS_FOLDER):
                        with Image.open(os.path.join(BALLS_FOLDER, filename)) as reference_image:
                            if sent_image.size == reference_image.size and sent_image.tobytes() == reference_image.tobytes():
                                filename_without_ext = os.path.splitext(filename)[0].split(".")[-1]
                                await message.channel.send(f"Match Found : {filename_without_ext}")

                                os.remove("Temp.jpg")
                                return

                await message.channel.send("No Match Found")

            except Exception as e:

                print(f"Error: {e}")

                await message.channel.send("An Error Occured Processing The Image")
                os.remove("Temp.jpg")

    await bot.process_commands(message)


bot.run("MTE5MDg4NjgxMTY3MzgzNzY3OA.Gu22wg.GwG2jhJfhnhWc0AmyiSKfDTQTs_f8W7p4oRegs")
