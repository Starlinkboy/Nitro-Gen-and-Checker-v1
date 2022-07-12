#Love - Starlinkboy
#For queries contact TheStarlinkGirl#5014 on discord
from pystyle import *
import requests, random, threading, string, os
print(Colorate.Horizontal(Colors.blue_to_red, """


███████╗████████╗ █████╗ ██████╗ ██╗     ██╗███╗   ██╗██╗  ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║████╗  ██║██║ ██╔╝
███████╗   ██║   ███████║██████╔╝██║     ██║██╔██╗ ██║█████╔╝ 
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║╚██╗██║██╔═██╗ 
███████║   ██║   ██║  ██║██║  ██║███████╗██║██║ ╚████║██║  ██╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                              
   
                                                                                        
"""))
print(Colorate.Horizontal(Colors.blue_to_red,"Version 1 : Basic generator and checker"))
threads = input(Colorate.Horizontal(Colors.blue_to_red, "Start by typing any number: "))
# ---
os.system(f'Nitro Generator v1.0 | Starlinkboy')
def nitro():
    while True:
     f=open("valid nitro.txt", "w", encoding='utf-8')
     code = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
     r = requests.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true')
     if r.status_code == 200:
         print(Colorate.Horizontal(Colors.blue_to_red, f'Valid Code! | discord.gift/{code}\n'))
         f.write(f"discord.gift/{code}\n")
     else:
         print(Colorate.Horizontal(Colors.blue_to_red, f'Invalid Code! | discord.gift/{code}\n'))
         
     
while True:
 if threading.active_count() < int(threads):
            threading.Thread(target=nitro).start()