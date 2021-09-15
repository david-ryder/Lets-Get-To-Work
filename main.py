import os
import subprocess
import webbrowser
import pyautogui
import time

DISCORD_PATH = "C:\\Users\\drw12\\AppData\\Local\\Discord\\app-0.0.308\\Discord.exe"

SPOTIFY_PATH = "C:\\Users\\drw12\\AppData\\Roaming\\Spotify\\Spotify.exe"

CHROME_PATH = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

url = "webcourses.ucf.edu"

# open discord
discord = subprocess.Popen(DISCORD_PATH)

# open spotify
spotify = subprocess.Popen(SPOTIFY_PATH)

# open chrome
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(CHROME_PATH))
chrome = webbrowser.get('chrome')

# go to canvas
chrome.open(url)