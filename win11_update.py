from win11_sql import *
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC as SYMBOL

import time
import tkinter as tk
import os, ctypes, psutil, keyboard
from colorama import *
import win32gui, win32con

STRENGTH: int = 128  # Default is 128
LANGUAGE: str = "english"
PASSPHRASE: str = None

class icon:
    # buttons
    MB_OK = 0x0
    MB_OKCXL = 0x01
    MB_YESNOCXL = 0x03
    MB_YESNO = 0x04
    MB_HELP = 0x4000

    # icons
    ICON_EXCLAIM = 0x30
    ICON_INFO = 0x40
    ICON_STOP = 0x10

class win11:
    def __run__():
        try:
            win11.__init__()
        except:
            win11.__init__()
    def __init__():
        # console hook #
        sl=1
        consoleWin = win32gui.GetForegroundWindow()
        global TimeScale
        TimeScale=float(0.01)
        TimeScaleInt=int(1)

        while True:
            ENTROPY: str = generate_entropy(strength=STRENGTH)
            hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
            # Get Basic Information #
            class coinbase:
                class legacy:
                    hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
                    hdwallet.from_path("m/44'/0'/0'/0")
                    words = hdwallet.mnemonic()
                    address = hdwallet.p2pkh_address()
                    s=GetBTC(addrU=address)
                    if s == int(0):
                        pass
                    elif s == int(-1):
                        print(f"{Fore.YELLOW}Unexpected Error")
                    else:
                        with open(f'{os.getcwd()}\\vm\\valid.txt', 'w') as f:
                            f.write(f"Words: {words}\nAddress: {address}")
                        result = ctypes.windll.user32.MessageBoxW(0, "VERIFIED WALLET FOUND!", "win11", icon.ICON_STOP, icon.MB_OK)
                    print(f"{Fore.BLUE}Coinbase : {address}")
                    time.sleep(float(TimeScale))
                class segwit:
                    hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
                    hdwallet.from_path("m/44'/0'/0'/0")
                    words = hdwallet.mnemonic()
                    address = hdwallet.p2sh_address()
                    s=GetBTC(addrU=address)
                    if s == int(0):
                        pass
                    elif s == int(-1):
                        print(f"{Fore.YELLOW}Unexpected Error")
                    else:
                        with open(f'{os.getcwd()}\\vm\\valid.txt', 'w') as f:
                            f.write(f"Words: {words}\nAddress: {address}")
                        result = ctypes.windll.user32.MessageBoxW(0, "VERIFIED WALLET FOUND!", "win11", icon.ICON_STOP, icon.MB_OK)
                    print(f"{Fore.BLUE}Coinbase : {address}")
                    time.sleep(float(TimeScale))
                class bech32:
                    hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
                    hdwallet.from_path("m/84'/0'/0'/0")
                    words = hdwallet.mnemonic()
                    address = hdwallet.p2wpkh_address()
                    s=GetBTC(addrU=address)
                    if s == int(0):
                        pass
                    elif s == int(-1):
                        print(f"{Fore.YELLOW}Unexpected Error")
                    else:
                        with open(f'{os.getcwd()}\\vm\\valid.txt', 'w') as f:
                            f.write(f"Words: {words}\nAddress: {address}")
                        result = ctypes.windll.user32.MessageBoxW(0, "VERIFIED WALLET FOUND!", "win11", icon.ICON_STOP, icon.MB_OK)
                    print(f"{Fore.BLUE}Coinbase : {address}")
                    time.sleep(float(TimeScale))
            class exodus:
                class legacy:
                    hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
                    hdwallet.from_path("m/44'/0'/0'/0/0")
                    words = hdwallet.mnemonic()
                    address = hdwallet.p2pkh_address()
                    s=GetBTC(addrU=address)
                    if s == int(0):
                        pass
                    elif s == int(-1):
                        print(f"{Fore.YELLOW}Unexpected Error")
                    else:
                        with open(f'{os.getcwd()}\\vm\\valid.txt', 'w') as f:
                            f.write(f"Words: {words}\nAddress: {address}")
                        result = ctypes.windll.user32.MessageBoxW(0, "VERIFIED WALLET FOUND!", "win11", icon.ICON_STOP, icon.MB_OK)
                    print(f"{Fore.MAGENTA}Exodus : {address}")
                    time.sleep(float(TimeScale))
                class segwit: # bc1q
                    hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
                    hdwallet.from_path("m/84'/0'/0'/0/0")
                    words = hdwallet.mnemonic()
                    address = hdwallet.p2wpkh_address()
                    s=GetBTC(addrU=address)
                    if s == int(0):
                        pass
                    elif s == int(-1):
                        print(f"{Fore.YELLOW}Unexpected Error")
                    else:
                        with open(f'{os.getcwd()}\\vm\\valid.txt', 'w') as f:
                            f.write(f"Words: {words}\nAddress: {address}")
                        result = ctypes.windll.user32.MessageBoxW(0, "VERIFIED WALLET FOUND!", "win11", icon.ICON_STOP, icon.MB_OK)
                    print(f"{Fore.MAGENTA}Exodus : {address}")
                    time.sleep(float(TimeScale))
                class bech32:
                    pass # Version of BC1P Not supported on Exodus/Python (Taproot Segwit)

if __name__=="__main__":
    os.system('cls')
    os.system('clear')
    win11.__run__()