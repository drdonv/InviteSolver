import pyperclip
import re
import pyautogui

line = input("Enter string: ")
line = line.replace("https://discord.gg/", "")
line = line.replace("discord.gg/", "")
line = re.sub('[\W_]+', '', line)


#pyperclip.copy("<@456989590708813824>")
#for  x in range(100):
#    pyperclip.paste()
#    pyautogui.press('enter')


print("https://discord.gg/" + line)
pyperclip.copy("discord.gg/" + line)