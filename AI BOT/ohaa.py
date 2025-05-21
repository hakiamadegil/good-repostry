import discord
from discord.ext import commands
import os
from tungutngtungtungsahuur import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)  # Klasör yoksa oluştur

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            

            file_name= attachment.filename
            file_path=os.path.join(IMAGE_DIR, file_name)

            try:
                await attachment.save(file_path)
                await ctx.send(f"Görsel Kaydedildi: {file_name}")
                class_name, confidence_score =get_class(file_path)
                await ctx.send(f"🔍 Sınıflandırma sonucu: `{class_name}`\n🔍 Güven skoru: `{confidence_score:.2f}`")

                cikarimlar={"If":"bu bir eğer komudu",
                            "Else":"if kmutundan sonra kullanılır",
                            "Print":"bunla birşeyler yazarız"}
                cikarim=cikarimlar.get(class_name, "bunun daha bilgisi yok")
            except:
                await ctx.send(f"Görsel kaydedilmedi üühühhü: {file_name}")
    else:
        await ctx.send("görsel yükle lannnn")

bot.run("çalma")