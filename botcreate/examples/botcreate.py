filename = input("File name: ")
command_prefix= input("What do you want your command prefix to be: ")
number_of_commands = int(input("How many commands do you want: "))
with open(filename, "w") as f:
    f.write("import disnake\nfrom disnake.ext import commands\n")
    f.write(f"""
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("{command_prefix}"),
    intents=disnake.Intents.all(),
    case_insensitive=True,
)""")
    for i in range(number_of_commands):
        command_name = input("name of command: ")
        command_description = input("command description: ")
        number_of_args = int(input("Number of args: "))
        f.write(f"""
@bot.slash_command(name="{command_name}", description="{command_description}")
""")    
        f.write("async def num(inter: disnake.ApplicationCommandInteraction")
        for i in range(number_of_args):
            arg_name = input("Arg name: ")
            arg_type = input("Type of arg: ")
            f.write(f", {arg_name}:{arg_type}")
        f.write("):\n")
        f.write("""
    try:
        #*********
        # Perform your desired operation with your args here
        result = None # set to None as default


        #*********
        embed = disnake.Embed(title="Operation Result", description=f"The result of the operation is: {result}", color=0x00ff00)
        await inter.response.send_message(embed=embed, ephemeral=True)\n
""")
        error_handling_bool = bool(input("do you want error handiling, enter True or False: "))
        if error_handling_bool == True:
            f.write("""
    except Exception as e:
        embed = disnake.Embed(title="Error", description=f"An error occurred: {e}", color=0xff0000)
        await inter.response.send_message(embed=embed, ephemeral=True)


""")