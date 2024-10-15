import ctypes

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

class system:
    def msgBox(text, title):
        result = ctypes.windll.user32.MessageBoxW(0, text, title, MB_OK | ICON_INFO)