import pyperclip
import re
import win32clipboard
import keyboard
import pyautogui
import time

keyboard.wait("ALT")
win32clipboard.OpenClipboard()
line = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

#line = input("Enter string: ")
line = line.replace("https://discord.gg/", "")
line = line.replace("discord.gg/", "")
line = re.sub('[\W_]+', '', line)

print("https://discord.gg/" + line)
pyperclip.copy("discord.gg/" + line)
pyautogui.hotkey('ctrl', 'v', interval = 0.15)
#time.sleep(0.05)
pyautogui.press('enter')
