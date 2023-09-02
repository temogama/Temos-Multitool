import requests
import os
import sys
from colorama import Fore
print(Fore.CYAN+"""
  _    _      _    _____ _                _                       
 | |  | |    | |  / ____| |              | |                      
 | |  | |_ __| | | (___ | |__   ___  _ __| |_ ___ _ __   ___ _ __ 
 | |  | | '__| |  \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
 | |__| | |  | |  ____) | | | | (_) | |  | ||  __/ | | |  __/ |   
  \____/|_|  |_| |_____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|   
                                                                  
            [+] - Temo`s Mutlitool - [+]                                                                  
""")

url = input("~/# Enter URL :")

tiny = 'http://tinyurl.com/api-create.php?url=' + url
info = requests.get(tiny)

def exit_menu(command):
    if command == 'tn':
        os.system('cmd /k "python main.py"' if os.name == 'nt' else 'python main.py')
        
while True:
    print("~/# Link :" + info.text)
    print("~/ Thanks For Using Tool!\nType 'tn' to go back in main menu!")