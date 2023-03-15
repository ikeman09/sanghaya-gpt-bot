from dotenv import load_dotenv
import discord
import os
from src.model.openai import gpt_response
from discord.ext import commands
import openai

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

prefix = "!"
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.command()
async def sgpt(ctx, *, args):
    try:
        response, tokens_used = gpt_response(prompt=args)
        await ctx.send(f"{response}\n\n **Number of tokens used: {tokens_used}**")
    except openai.error.RateLimitError as e:
        if e.http_status == 429:
            print("The model is currently overloaded. Please try again later.")
            await ctx.send("The model is currently overloaded. Please try again later.")
        else:
            await ctx.send("Unknown error has occured.")
