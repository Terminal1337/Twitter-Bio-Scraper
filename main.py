import httpx
import json
import threading
from colorama import Fore, init
from helpers.const import *
from helpers.utils import *

init(convert=True)
__lock__ = threading.Lock()
class Twitter:
    def __init__(self) -> None:
        self.threads = int(input("Threads: "))
        self.min_followers = int(input("Minimum followers: "))
        self.usernames = open('input/usernames.txt', 'r').read().splitlines()
        
    def scrape(self,username : str):
        try:
            resp = get_followers(screen_name=username,min_followers=self.min_followers)
        except:
            return
        if not resp[0] or not resp[2]:
            with __lock__:
                print(f"{Fore.RED}INFO : {Fore.RESET} {Fore.YELLOW}[{username}]{Fore.RESET}{Fore.LIGHTRED_EX} has less than ({self.min_followers}) followers{Fore.RESET} [{resp[1]}]")
            return
        with open('output/scraped.txt','a',encoding='utf-8') as f:
            f.write(f"{username}:{resp[2]}\n")
            f.close()
        with __lock__:
            print(f"{Fore.RED}INFO : {Fore.RESET} {Fore.YELLOW}[{username}]{Fore.RESET}{Fore.GREEN} has ({resp[1]}) followers and ({resp[2]}) domain{Fore.RESET}")
        return
        

    def startThreads(self):
        for username in self.usernames:
            threading.Thread(target=self.scrape, args=(username,)).start()
            if threading.active_count()>= self.threads:
                while True:
                    if threading.active_count() < self.threads:
                        break
        print(f"{Fore.GREEN}INFO : {Fore.RESET} Finished scraping{Fore.RESET}")
        
    

                
                
if __name__ == "__main__":
    r = Twitter()
    r.startThreads()