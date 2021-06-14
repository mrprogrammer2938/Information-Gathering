#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
import sys
import requests
import ipapi
import socket
import json
import subprocess
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[96m'
    darkblue = '\033[34m'
    org = '\033[33m'
    line = '\033[4m'
opt = "\nInformation-Gathering/> "
ip = "\nEnter ip: "
def cls():
    os.system("clear")
def title():
    os.system("printf '\033]2;Information Gathering\a'")
def menu():
    title()
    cls()
    banner()
    menu_list()
def banner():
    print(color.green + """
░▀█▀░█▀█░█▀▀░█▀█░█▀▄░█▄█░█▀█░▀█▀░▀█▀░█▀█░█▀█░░░█▀▀░█▀█░▀█▀░█░█░█▀▀░█▀▄░▀█▀░█▀█░█▀▀
░░█░░█░█░█▀▀░█░█░█▀▄░█░█░█▀█░░█░░░█░░█░█░█░█░░░█░█░█▀█░░█░░█▀█░█▀▀░█▀▄░░█░░█░█░█░█""" + color.red + " Version: " + color.blue + "1.3.0" + color.green + """
░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░▀░▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀ \n""" + color.End)
def menu_list():
    print("\n{1}.Online Attack")
    print("{2}.Information Gathering Tools")
    print("{3}.Developer")
    print("{4}.Exit")
    choose = input(opt)
    if choose == '1':
        menu2()
    elif choose == '2':
        menu3()
    elif choose == '3':
        dev()
    elif choose == '4':
        ext()
    elif choose == '':
        menu()
    elif choose == ' ':
        menu()
    elif choose == '  ':
        menu()
    else:
        cls()
        print(choose + color.red + " Not Found!" + color.End)
        try_to_menu1()
def try_to_menu1():
    try1 = input("\npress Enter...")
    if try1 == '':
        menu()
    else:
        menu()
def menu2():
    cls()
    os.system("figlet -f slant Information Gathering|lolcat")
    print("\n{1}.Port-Scan")
    print("{2}.Whois lookup")
    print("{3}.nslookup")
    print("{4}.Ping")
    print("{5}.Web Location")
    print("{99}.mein menu")
    choose2 = input(opt)
    if choose2 == '1':
        Information_Gathering_portscan()
    elif choose2 == '2':
        Information_Gathering_whois()
    elif choose2 == '3':
        Information_Gathering_nslookup()
    elif choose2 == '4':
        Information_Gathering_ping()
    elif choose2 == '5':
        Information_Gathering_webloc()
    elif choose2 == '99':
        menu()
    else:
        menu2()
def menu3():
    cls()
    os.system("figlet -f slant Tools|lolcat")
    print("\n{1}-nmap")
    print("{2}-Web Info")
    print("{3}-Info G")
    print("{4}-Th3inspector")
    print("{5}-Dark side")
    print("{6}-BillCipher")
    print("{99}-mein menu")
    choose3 = input(opt)
    if choose3 == '1':
        cls()
        os.system("git clone https://github.com/nmap/nmap")
        try2()
    elif choose3 == '2':
        cls()
        os.system("git clone https://github.com/mrprogrammer2938/Web-Info")
        try2()
    elif choose3 == '3':
        cls()
        os.system("git clone https://github.com/haijuga7/InfoG")
        try2()
    elif choose3 == '4':
        cls()
        os.system("git clone https://github.com/Moham3dRiahi/Th3inspector")
        try2()
    elif choose3 == '5':
        cls()
        os.system("git clone https://github.com/ultrasecurity/DarkSide")
        try2()
    elif choose3 == '6':
        cls()
        os.system("git clone https://github.com/GitHackTools/BillCipher")
        try2()
    elif choose3 == '99':
        menu()
    else:
        menu3()
def dev():
    cls()
    print(color.blue)
    os.system("figlet Developer")
    print(color.End)
    print(color.red + "\nThis code write by " + color.green + "Mr.nope" + color.End)
    print(color.red + "\nVersion: " + color.org + "1.3.0" + color.End)
    print(color.darkblue + "\nGithub: " + color.line + "https://github.com/mrprogrammer2938" + color.End)
    time.sleep(2)
    try3()
def try3():
    try_to_menu2 = input("\npress Enter...")
    if try_to_menu2 == '':
        menu()
    else:
        menu()
def ext():
    cls()
    print(color.green + "Exiting..." + color.End)
    sys.exit()
def Information_Gathering_ping():
    cls()
    host = input(ip)
    time.sleep(1)
    packet = input(packet)
    time.sleep(1)
    s = subprocess.getoutput("ping -w " + packet + " " + host)
    print(s)
    try4()
def try4():
    try_again_1 = input("Do you want to try again? [y/n] ")
    if try_again_1 == 'y':
        Information_Gathering_ping()
    elif try_again_1 == 'n':
        try6()
    else:
        try4()
def Information_Gathering_whois():
    cls()
    host2 = input(ip)
    time.sleep(1)
    print(color.org)
    s2 = subprocess.getoutput("whois " + host2)
    print(s2)
    try5()
def try5():
    try_again_2 = input("Do you want to try again? [y/n] ")
    if try_again_2 == 'y':
        Information_Gathering_whois()
    elif try_again_2 == 'n':
        try6()
    else:
        try5()
def try6():
    try_to_menu3 = input("\npress Enter...")
    if try_to_menu3 == '':
        menu2()
    else:
        menu2()
def Information_Gathering_nslookup():
    cls()
    host3 = input(ip)
    time.sleep(1)
    s3 = subprocess.getoutput("nslookup " + host3)
    try7()
def try7():
    try_to_menu4 = input("\npress Enter...")
    if try_to_menu4 == '':
        menu2()
    else:
        menu2()
def Information_Gathering_webloc():
    cls()
    host4 = input(ip)
    time.sleep(1)
    search = ipapi.location(ip=host4, key=None)
    try:
       print("\n")
       print(Fore.RED + "[~] " + Fore.WHITE + "Ip: " + Fore.GREEN + search["ip"])
       print(Fore.RED + "[~] " + Fore.WHITE + "City " + Fore.GREEN + search["city"])
       print(Fore.RED + "[~] " + Fore.WHITE + "Region " + Fore.GREEN + search["region"])
       print(Fore.RED + "[~] " + Fore.WHITE + "Country: " + Fore.GREEN + search["country"])
       print(Fore.RED + "[~] " + Fore.WHITE + "Org: " + Fore.GREEN + search["org"])
       print(Fore.RED + "[~] " + Fore.WHITE + "Time Zone: " + Fore.GREEN + search["timezone"])
       print(Fore.RED + "[~] " + Fore.WHITE + "Languages: " + Fore.GREEN + search["languages"])
       time.sleep(2)
       try8()
    except:
        print("\nStoping...")
        try7()
def try8():
    try_to_menu5 = input("Do you want to try again? [y/n] ")
    if try_to_menu5 == 'y':
        Information_Gathering_webloc()
    elif try_to_menu5 == 'n':
        try7()
    else:
        try8()
def Information_Gathering_portscan():
    cls()
    os.system("git clone https://github.com/mrprogrammer2938/Portscan")
    try7()
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print(color.red + "\nExiting...\n" + color.End)
        sys.exit()
