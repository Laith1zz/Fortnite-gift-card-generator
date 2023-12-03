#Script is made by The Mag Market and dropped for free
#IF YOU HAVE PAID FOR THIS YOU HAVE GOTTEN SCAMMED
#https://discord.gg/P8sKTTndqk

import requests
import random
import string
from colorama import init, Fore as cc
from pystyle import Center
import os
from datetime import datetime

init()
r = R = cc.RED
print(f'{r}')

logo = Center.XCenter("""
  _____ _        __  __           __  __          _       _   
 |_   _| |_  ___|  \/  |__ _ __ _|  \/  |__ _ _ _| |_____| |_ 
   | | | ' \/ -_) |\/| / _` / _` | |\/| / _` | '_| / / -_)  _|
   |_| |_||_\___|_|  |_\__,_\__, |_|  |_\__,_|_| |_\_\___|\__|
                            |___/   Made by magcecu  
                                             
                    Fortnite Gift Card Miner              
                                                           """)

os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

n = int(input("How Many Codes Should We Generate>>> "))

os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

def main():
    characters = string.ascii_uppercase + string.digits
#    code = ''.join(random.choice(characters) for _ in range(4)) + '-' + ''.join(random.choice(characters) for _ in range(4)) + '-' + ''.join(random.choice(characters) for _ in range(4)) + '-' + ''.join(random.choice(characters) for _ in range(4))
    code = ''.join(random.choice(characters) for _ in range(16))
    response = requests.get(f"https://api.fortnite.com/check_code?code={code}")

    if response.status_code == 200:
        print(f' {code} | VALID !!!!!!!!!!! Saving in valid.txt...')
        with open('valid.txt', 'w') as file:
             file.write(f"{code} is valid\n")
    if response.status_code == 429:
        print(" RATE LIMIT HIT") #TURNS OUT THERE IS NO RATE LIMIT
    if response.status_code == 404:
        print(' Network/Server error')
    else:
        print(f' {code} | INVALID')

for i in range(n):
    main()
    i + 1

current_time = datetime.now()
print("")
print(Center.XCenter(f"Mine Has Ended! {current_time}"))