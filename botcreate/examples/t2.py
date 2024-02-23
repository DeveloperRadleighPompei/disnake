import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)
@bot.slash_command(name="Terry", description="Terry")
async def num(inter: disnake.ApplicationCommandInteraction, Terry:str, Terry2:str):

    try:
        #*********
        # Perform your desired operation with your args here
        result = Terry+Terry2 # set to None as default


        #*********
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)


    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)



@bot.slash_command(name="Timmy", description="Timmy")
async def num(inter: disnake.ApplicationCommandInteraction, Timmy:str, Timmy2:str):

    try:
        #*********
        # Perform your desired operation with your args here
        result = None # set to None as default


        #*********
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)


    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)


#