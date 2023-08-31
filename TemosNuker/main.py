import sys,os
from colorama import Fore
import discord
from discord.ext import commands


print(Fore.CYAN+"""  _______                   _       _   _       _             
 |__   __|                 ( )     | \ | |     | |            
    | | ___ _ __ ___   ___  \|___  |  \| |_   _| | _____ _ __ 
    | |/ _ \ '_ ` _ \ / _ \  / __| | . ` | | | | |/ / _ \ '__|
    | |  __/ | | | | | (_) | \__ \ | |\  | |_| |   <  __/ |   
    |_|\___|_| |_| |_|\___/  |___/ |_| \_|\__,_|_|\_\___|_|   
                                                              
                                                              """)
print(Fore.MAGENTA+"[+] - - - - - Welcome to Temo`s Nuke World! - - - - - [+]")

def display_menu():
    print(Fore.RED + """[+] - - - Choose Option - - - [+]""")
    print(Fore.GREEN + """[1] - Nuke Server \n[2] - Ip Lookup\n[3] - About Us""")

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python NukeBot/nuker.py"' if os.name == 'nt' else 'python NukeBot/nuker.py')
    elif command == '2':
        os.system('cmd /k "python iplookup/ip-lookup.py"' if os.name == 'nt' else 'python iplookup/ip-lookup.py')
    elif command == '3':
        print("Join our discord server! - https://discord.gg/Nr7PdYfaQe - ")
    else:
        print(Fore.RED+"Invalid option!")

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
