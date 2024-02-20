import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)

@bot.slash_command(name="num", description="Performs an operation with two numbers")
async def num(inter: disnake.ApplicationCommandInteraction, num1: int, num2: int):
    try:
        # Perform your desired operation with num1 and num2
        result = num1 + num2  # Example: You can perform any operation you want here

        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)
    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)

@bot.command()
async def add(ctx: commands.Context, left: int, right: int):
    """Adds two numbers together."""
    embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {left+right}", color=0x00ff00)
    await ctx.response.send_message(embed=embed, ephemeral=True)
bot.run("MTIwOTIyNjEyNjQyMjA1Njk5MQ.GGkTRn.HKKn562XlpUi_PxRd3M4EnFb0doA6XLxbH8gVw")
