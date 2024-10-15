from win11_sql import *

import time
import tkinter as tk
import os, ctypes, psutil, keyboard
from colorama import *
import win32gui, win32con

from bit import *
from bit.format import bytes_to_wif
import random
import urllib.request
import requests

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
        # gui #
        try:
            root.destroy()
        except:
            pass
        root = tk.Tk()
        root.overrideredirect(True)
        root.geometry("150x20+{:d}+{:d}".format(root.winfo_screenwidth()-150,0))

        # Configure the label font to look pixelated
        font = ("Courier", 12, "bold")
        root.option_add("*Font", font)

        # Create the label that displays the CPU usage percentage
        label = tk.Label(root, text="", bg="green", fg="white", anchor="w", justify="left")
        label.pack(fill="both", expand=True, anchor="w")

        # Function to update the CPU usage percentage
        def update_cpu_usage():
            cpu_percent = psutil.cpu_percent(interval=None, percpu=False)
            space="     "
            label.config(text=f"{TimeScale}      {str(cpu_percent).replace('.','')}%")
            root.after(1000, update_cpu_usage)

        # Start updating the CPU usage percentage
        update_cpu_usage()
        while True:
            x=1
            y=115792089237316195423570985008687907852837564279074904382605163141518161494336
            ran= random.randint(x,y)
            key = Key.from_int(ran)
            seed=str(ran)
            wif = bytes_to_wif(key.to_bytes(), compressed=False)
            wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
            key1 = Key(wif)

            class legacy_compressed:
                address = key.address #Legacy compressed address
                BRUTE(ad1=address, wif=wif, wif2=wif2, sl=sl)
            class legacy_uncompressed:
                address = key1.address #Legacy uncompressed address
                BRUTE(ad1=address, wif=wif, wif2=wif2, sl=sl)
            class segwit:
                address = key.segwit_address  #Segwit address
                BRUTE(ad1=address, wif=wif, wif2=wif2, sl=sl)
            time.sleep(float(TimeScale))


            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('+'):
                TimeScale=TimeScale+float(0.01)
                TimeScaleInt=TimeScaleInt+int(1)
                time.sleep(0.2)
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('-'):
                if TimeScale == float(0.01):
                    pass
                else:
                    TimeScale=TimeScale - float(0.01)
                    TimeScaleInt=TimeScaleInt - int(1)
                time.sleep(0.2)
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('p'):
                quit()
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('h'):
                if sl == 1:
                    sl=0
                    win32gui.ShowWindow(consoleWin , win32con.SW_HIDE)
                elif sl == 0:
                    sl=1
                    win32gui.ShowWindow(consoleWin , win32con.SW_SHOW)
                time.sleep(0.2)
            if TimeScale == float(0.01) or TimeScale == float(0.02) or TimeScale == float(0.03) or TimeScale == float(0.04) or TimeScale == float(0.05):
                pass
            else:
                TimeScale=float(0.01)
            root.update()


if __name__=="__main__":
    win11.__run__()