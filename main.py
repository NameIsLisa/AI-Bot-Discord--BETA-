import discord
from discord.ext import commands
from utils import get_class
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import random


try:
    model = load_model('Konverted_keras/keras_model.h5','keras_char/keras_model.h5', compile=False)
except Exception as e:
    print(f"Error loading model: {e}")


with open("token.txt", "r") as f: 
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Halo! Aku adalah bot {bot.user}!')

@bot.command()
async def perkenalkan_diri(ctx):
    await ctx.send(f'Namaku adalah {bot.user}! Aku adalah sebuah bot discord yang dibuat untuk membantu pengguna. Aku akan selalu dikembangkan, tunggu saja! aku pertama kali dibuat pada 2024 April!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

@bot.command()
async def visit_TouhouLWG(ctx):
    link = "https://global.touhoulostword.com"
    await ctx.send(f"Kamu bisa mengunjungi website TouhouLostWord Global resmi dengan klik link ini: {link}")

@bot.command()
async def commands(ctx):
    hint = "$check , $check_image , $hello , $heh , $visit_TouhouLW , $check_character , $fact"
    await ctx.send(f"{hint}")

# Fungsi untuk membuka game
def open_game():
    try:
        os.startfile("F:\PapersPlease\PapersPlease.exe")  # Ganti dengan path game kamu
    except Exception as e:
        print(f"Error saat membuka game: {e}")

# Command untuk membuka game
@bot.command()
async def PapersPlease(ctx): #ganti commnand nya(misalnya nama game nya)
    await ctx.send("Membuka Game....")
    open_game()


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Menyimpan gambar ke ./{attachment.filename}")
    else:
        await ctx.send("Unggah gambarnya dulu :D")

@bot.command()
async def check_image(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            try:
                result = get_class(model_path="Konverted_keras/keras_model.h5", labels_path="Konverted_keras/labels.txt", image_path=f"./{attachment.filename}")
                await ctx.send(result)
            except Exception as e:
                await ctx.send(f"Terjadi kesalahan saat memproses gambar: {str(e)}")
    else:
        await ctx.send("Unggah gambarnya dulu :D")

@bot.command()
async def check_character(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            try:
                result = get_class(model_path="keras_char/keras_model.h5", labels_path="keras_char/labels.txt", image_path=f"./{attachment.filename}")
                await ctx.send(result)
            except Exception as e:
                await ctx.send(f"Terjadi kesalahan saat memproses gambar: {str(e)}")
    else:
        await ctx.send("Unggah gambarnya dulu :D")

@bot.command()
async def fact(ctx):
    random_fact = random.choice(facts)
    await ctx.send(random_fact)


facts = [
    "Madu tidak pernah rusak. Para arkeolog telah menemukan pot berisi madu di makam Mesir kuno yang berusia lebih dari 3000 tahun dan masih dapat dimakan!",
    "Sehari di Venus lebih lama dari satu tahun di Venus. Venus membutuhkan 243 hari Bumi untuk berputar pada porosnya, tetapi hanya 225 hari Bumi untuk mengorbit Matahari.",
    "Gurita mempunyai tiga jantung, dua jantung memompa darah ke insang, sedangkan satu memompa darah ke seluruh tubuh.",
    "Pisang itu buah beri, tapi stroberi bukan!",
    "Hiu sudah ada sebelum pohon. Hiu telah ada sejak 400 juta tahun yang lalu, sedangkan pohon paling awal muncul sekitar 350 juta tahun yang lalu.",
    "Manusia dan jerapah memiliki jumlah tulang leher yang sama – keduanya memiliki tujuh.",
]



bot.run(token)  
    