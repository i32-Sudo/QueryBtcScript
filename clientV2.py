import scan.integrity.BTC.src as i_btc
import scan.integrity.ETH.src as i_eth

import scan.mneomic.BTC.src as u_btc
import scan.mneomic.ETH.src as u_eth

import os
from multiprocessing import Process
import ctypes

from colorama import *


class script:
    def __init__():
        os.system('cls')
        content=f"""

{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}b1{Fore.LIGHTMAGENTA_EX}]{Fore.WHITE}  Bitcoin Wallet from Random Generation  [BTC]
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}b2{Fore.LIGHTMAGENTA_EX}]{Fore.WHITE}  Bitcoin Wallet from Mneomic Generation [BTC]
        """;print(content)
        s=input(f" {Fore.LIGHTMAGENTA_EX}Option >{Fore.WHITE}     ")
        if s == 'b1':
            threads=input(f" {Fore.LIGHTMAGENTA_EX}Threads >{Fore.WHITE}     ")
            for _ in range(int(threads)):
                pi = Process(target=i_btc.script.run).start()
        elif s == 'b2':
            threads=input(f" {Fore.LIGHTMAGENTA_EX}Threads >{Fore.WHITE}     ")
            for _ in range(int(threads)):
                pi = Process(target=u_btc.script.run).start()
if __name__=="__main__":
    script.__init__()