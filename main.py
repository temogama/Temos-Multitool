import sys,os
from colorama import Fore
import discord
from discord.ext import commands


print(Fore.CYAN+"""
  _______                   _       __  __       _ _   _ _              _ 
 |__   __|                 ( )     |  \/  |     | | | (_) |            | |
    | | ___ _ __ ___   ___  \|___  | \  / |_   _| | |_ _| |_ ___   ___ | |
    | |/ _ \ '_ ` _ \ / _ \  / __| | |\/| | | | | | __| | __/ _ \ / _ \| |
    | |  __/ | | | | | (_) | \__ \ | |  | | |_| | | |_| | || (_) | (_) | |
    |_|\___|_| |_| |_|\___/  |___/ |_|  |_|\__,_|_|\__|_|\__\___/ \___/|_|
                                                                          
                                                                          
""")
print(Fore.MAGENTA+"[+] - - - - - Welcome to Temo`s Multitool World! - - - - - [+]\n- - - - - - - - - - Thanks to: Gravity - - - - - - - - - -\n\n")


def display_menu():
    print(Fore.BLUE + """       [+] -| -| -| _ Options _ |- |- |- [+]                   """)
    print(Fore.GREEN + """[1] - Nuke Server           [6] - Url Shortener  \n[2] - Phone Lookup  \n[3] - Ip-Tracker  \n[4] - Zip-Cracker\n[5] - Webhook Spam\n """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python nuker.py"' if os.name == 'nt' else 'python nuker.py')
    elif command == '2':
         os.system('cmd /k "python phonelocator.py"' if os.name == 'nt' else 'python phonelocator.py')
    elif command == '3':
        os.system('cmd /k "python ip-tracker.py' if os.name == 'nt' else 'python ip-tracker.py')
    elif command == '4':
         os.system('cmd /k "python zipcrack.py' if os.name == 'nt' else 'python zipcrack.py')
    elif command == '5':
        os.system('cmd /k "python webhookspam.py' if os.name == 'nt' else 'python webhookspam.py')
    elif command == '6':
        os.system('cmd /k "python urlshorten.py' if os.name == 'nt' else 'python urlshorten.py')

        
while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)