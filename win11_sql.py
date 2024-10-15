import psycopg2, ctypes, os
from colorama import *

#PostgreSQL Server Settings #
address = 'address'
conn = psycopg2.connect(dbname="bitcoin", user='admin',
                        password='1234', host='140.82.60.186', port=5432)
cursor = conn.cursor()
table = "hunter"

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

# Function to Get BTC and Return Value of Wallet #
def GetBTC(addrU):
    try:
        query = "SELECT * FROM " + table + " WHERE address = '" + addrU + "';"
        cursor.execute(query)
        try:
            res = cursor.fetchall()
            return str(res[0]).replace("'", "").replace("(", "").replace(",)", "")
        except: 
            return 0
    except:
        return -1
    
def BRUTE(ad1, wif, wif2, sl):
    s=GetBTC(addrU=ad1)
    if s == int(0):
        pass
    elif s == int(-1):
        print(f"{Fore.YELLOW}Unexpected Error")
    else:
        with open(f'{os.getcwd()}\\vm\\valid.txt', 'w') as f:
            f.write(f"Address: {ad1}\nPrivate Key Compressed: {wif2}\nPrivate Key Uncompressed: {wif}")
        result = ctypes.windll.user32.MessageBoxW(0, "VERIFIED WALLET FOUND!", "win11", icon.ICON_STOP, icon.MB_OK)
    if sl == 1:
        print(f"{Fore.MAGENTA}Wallet : {ad1}")
    else:
        pass