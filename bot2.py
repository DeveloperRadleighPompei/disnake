import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)
@bot.slash_command(name="one", description="one")

@bot.slash_command(name="two", description="two")

@bot.slash_command(name="three", description="three")
