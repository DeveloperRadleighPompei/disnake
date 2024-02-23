import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)
@bot.slash_command(name="", description="")
async def num(inter: disnake.ApplicationCommandInteraction