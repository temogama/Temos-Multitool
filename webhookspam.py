import requests
from colorama import Fore
import threading
import time
import sys

def load_animation(): 
  
    
    load_str = "Loading..."
    ls_len = len(load_str) 
  
  
     
    animation = "|/-\\"
    anicount = 0
      
    
    counttime = 0        
      
     
    i = 0                     
  
    while (counttime != 30): 
          
        
        time.sleep(0.075)  
                              
        
        load_str_list = list(load_str)  
          
         
        x = ord(load_str_list[i]) 
          
         
        y = 0                             
  
          
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1

def banner_display():
    print(Fore.CYAN+"""
 __          __  _     _                 _       _____                       
 \ \        / / | |   | |               | |     / ____|                      
  \ \  /\  / /__| |__ | |__   ___   ___ | | __ | (___  _ __   __ _ _ __ ___  
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  \___ \| '_ \ / _` | '_ ` _ \ 
    \  /\  /  __/ |_) | | | | (_) | (_) |   <   ____) | |_) | (_| | | | | | |
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_____/| .__/ \__,_|_| |_| |_|
                                                      | |                    
                                                      |_|                    
            [+] - Temo`s Multitool - [+]
      """)


def spam(msg, webhook):
    for i in range(30):
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook: " + webhook)
            exit()

while True:
    load_animation()
    banner_display()
    msg = input("Please Insert webhook Spam Message: ")
    webhook = input("Please Insert webhook URL: ")