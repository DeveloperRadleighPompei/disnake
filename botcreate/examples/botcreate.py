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
        f.write("):")