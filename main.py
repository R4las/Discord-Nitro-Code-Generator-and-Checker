import random, string
import webbrowser
import time
import requests
import datetime as dt
from colorama import init
from colorama import Fore, Back, Style
import os

class bcolors:
    BOLD = '\033[1m'

def main():
    print("""
    ███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░██╗███████╗████████╗
    ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██║██╔════╝╚══██╔══╝
    ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░██║█████╗░░░░░██║░░░
    ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██║██╔══╝░░░░░██║░░░
    ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝██║██║░░░░░░░░██║░░░
    ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░
    ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
    ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    ░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
    ░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
    ░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")


    time.sleep(0.2)
    print("                          Creator  -  R4las ")
    print(' ')
    time.sleep(0.1)
    num = input('How many codes to generate: ')
    time.sleep(0.1)
    select_nitro = input('Select nitro: (Boost or Classic):')
    time.sleep(0.1)
    select_mode = input('Automatically check code(y/n):')
    print(' ')

    t = dt.datetime.now()

    if select_mode == 'y':
        f = open("not_working_codes.txt", "w", encoding='utf-8')
        if select_nitro == 'Classic':
            for n in range(int(num)):
                y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
                f.write('https://discord.gift/')
                f.write(y)
                f.write("\n")

        if select_nitro == 'Boost':
            for n in range(int(num)):
                y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
                f.write('https://discord.gift/')
                f.write(y)
                f.write("\n")

        else:
            print('You have to write Boost or Classic not ' + select_nitro)

        f.close()

    elif select_mode == 'n':
        f2 = open('codes.txt', 'w', encoding='utf-8')
        if select_nitro == 'Classic':
            for n in range(int(num)):
                y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
                f2.write('https://discord.gift/')
                f2.write(y)
                f2.write("\n")

        if select_nitro == 'Boost':
            for n in range(int(num)):
                y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
                f2.write('https://discord.gift/')
                f2.write(y)
                f2.write("\n")

        else:
            print('You have to write Boost or Classic not '+select_nitro)

        f2.close()

    if select_mode == 'y':
        with open("not_working_codes.txt") as f:
            for line in f:
                nitro = line.strip("\n")

                url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                r = requests.get(url)

                if r.status_code == 200:
                    print(" Valid | {} ".format(line.strip("\n")))
                    r = open('valid_codes.txt','w')
                    r.writelines('https://discord.gift/' + y + '\n')
                    break
                else:
                    print(" Invalid | {} ".format(line.strip("\n")))
    elif select_mode == 'n':
        with open('codes.txt') as f:
            for line in f:
                print(line.strip('\n'))

    if select_mode == 'y' or select_mode == 'n':
        if select_mode == 'y':
            print(' ')
            print('Time spent for generating and checking codes:')
            print(dt.datetime.now()-t)
        if select_mode == 'n':
            print(' ')
            print('Time spent for generating codes:')
            print(dt.datetime.now()-t)
    else:
        print('You have to write y or n not '+select_mode)
    print(' ')
    riapri = input("Press Enter to close the program or digit R4 for restart it")
    if riapri == 'R4':
        print(os.system('main.py'))



main()
