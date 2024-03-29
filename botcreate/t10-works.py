import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)
@bot.slash_command(name="divide", description="divide")
async def num(inter: disnake.ApplicationCommandInteraction, num1:float, num2:float):

    try:
        #*********
        # Perform your desired operation with your args here
        result = num1/num2 
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)


    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)



@bot.slash_command(name="multiply", description="multiply")
async def num(inter: disnake.ApplicationCommandInteraction, num1:float, num2:float):

    try:
        #*********
        # Perform your desired operation with your args here
        result = num1*num2 # set to None as default


        #*********
        # embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=disnake.Colour.green())

        await inter.response.send_message(embed=embed, ephemeral=True)


    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)



@bot.slash_command(name="addition", description="add")
async def num(inter: disnake.ApplicationCommandInteraction, num1:float, num2:float):

    try:
        #*********
        # Perform your desired operation with your args here
        result = num1+num2 # set to None as default


        #*********
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)


    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)



@bot.slash_command(name="subtraction", description="subtract")
async def num(inter: disnake.ApplicationCommandInteraction, num1:float, num2:float):

    try:
        #*********
        # Perform your desired operation with your args here
        result = num1-num2 # set to None as default


        #*********
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)


    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)


bot.run("MTIwOTIyNjEyNjQyMjA1Njk5MQ.GVpbpe.Srg_uHGIQFe9R5ZLnLjNo77T03Zq_UkMttgr8M")
