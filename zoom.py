import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import keyboard,pyautogui
import pandas as pd
import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import time

def zstart():
    url="https://us04web.zoom.us/signin"
    #location of downloaded file.
    driver=webdriver.Chrome("C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe")
    driver.maximize_window()
    driver.get(url)
    text_area=driver.find_element_by_id("email")
    text_area.send_keys("abcd@gmail.com")
    time.sleep(0.25)
    ptextarea=driver.find_element_by_id("password")
    ptextarea.send_keys("abcd1234")
    time.sleep(2)
    element=driver.find_element_by_link_text("JOIN A MEETING")
    element.click()
    time.sleep(2)
    mtext_area=driver.find_element_by_id("join-confno")
    time.sleep(0.25)
    mtext_area.send_keys("572 079 9236")
    time.sleep(0.25)
    button=driver.find_element_by_id("btnSubmit")
    button.click()
    time.sleep(4)
    keyboard.send("tab",do_press=True,do_release=True)
    time.sleep(0.25)
    keyboard.send("tab",do_press=True,do_release=True)
    time.sleep(0.25)

    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(20)

    mtext=pyautogui.locateCenterOnScreen("mpass.PNG")
    pyautogui.moveTo(mtext)
    pyautogui.write("0dqbXp")
    print("abcdefgh")
    pyautogui.press('enter')
    time.sleep(25)
    jwa=pyautogui.locateOnScreen('jsa.PNG')
    pyautogui.moveTo(jwa)
    pyautogui.click()
    time.sleep(15)
    pyautogui.keyDown('alt')
    pyautogui.press('r')
    pyautogui.keyUp('alt')
    print("Thats all Folks")
    pyautogui.press('tab',presses=3)
    pyautogui.press('enter')
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
if __name__ == '__main__':
   print("Lets start")
   zstart()
