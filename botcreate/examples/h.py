import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)
@bot.slash_command(name="hi", description="hi")
async def num(inter: disnake.ApplicationCommandInteraction, hi:str):

 try:
        #*********
        # Perform your desired operation with your args here
        result = None # set to None as default


        #*********
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)

