from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from cs50 import get_int
from vip import is_vip
from time import sleep
import common as cm
import pandas as pd
import pyodbc as odbc
from win10toast import ToastNotifier
import ctypes
import pymsgbox
import pyautogui as pag
import clr                      #CLR from pythonnet is necessary to copy the files to clipboard
clr.AddReference('System.Collections.Specialized')
clr.AddReference('System.Windows.Forms')
from System.Collections.Specialized import StringCollection
from System.Windows.Forms import Clipboard
from fake_useragent import UserAgent

"""WHATBOT TESTS"""


def test1():
    def main():
        phone = '10101010'
        with open('numbers.txt', "w") as file:
            for i in range(100000):
                phone = nextNum(phone, '010')
                print(phone, file=file)
        phone = '10101010'
        print(one_and_one(phone))

    def nextNum(phone, starter):
            phone = int(phone) + 1
            phone = str(phone).zfill(8)
            return phone
    def is_vip(phone, starter):
                if one_and_one(phone) == True or beside_numbers(phone) == True or more_than_six(phone) == True or same_as_starter(phone, starter) == True:
                    return True
                return False
    def one_and_one(phone):
        if phone[0] == phone[4] and phone[2] == phone[6] and phone[1] == phone[5] and phone[3] == phone[7]:
            return True
        return False
    def semi_mirror(phone):
            if f'{phone[0]}{phone[1]}{phone[2]}' == f'{phone[5]}{phone[6]}{phone[7]}' or f'{phone[1]}{phone[2]}{phone[3]}' == f'{phone[4]}{phone[5]}{phone[6]}'or f'{phone[1]}{phone[2]}{phone[3]}' == f'{phone[5]}{phone[6]}{phone[7]}' or f'{phone[2]}{phone[3]}{phone[4]}' == f'{phone[5]}{phone[6]}{phone[7]}' or f'{phone[0]}{phone[1]}{phone[2]}' == f'{phone[4]}{phone[5]}{phone[6]}' or f'{phone[0]}{phone[1]}{phone[2]}' == f'{phone[3]}{phone[4]}{phone[5]}':
                return True
            return False
    def beside_numbers(phone):
        for i in range(10):
            if f'{i}{i}{i}{i}' in phone:
                return True
        return False
    def more_than_six(phone):
        for i in range(8):
            count = 0
            for j in range(10):
                if phone[i] == j:
                    count += 1
                    if count >= 6:
                        return True
        return False
    def same_as_starter(phone, starter):
        if (phone.startswith('0000') == True and starter == '010') or (phone.startswith('1111') == True and starter == '011') or (phone.startswith('2222') == True and starter == '012') or (phone.startswith('5555') == True and starter == '015'):
            return True
        return False
    main()

def headless():

    #OPTIONS SETUP
    options = Options()                     #Defining options for the driver
    options.add_experimental_option("detach", True)                     #Force the browser to stay open even after fininshing
    user_data_dir = r'C:\Users\ideapad\AppData\Local\Google\Chrome Dev\User Data'                       #Path for user data
    options.add_argument(f"--user-data-dir={user_data_dir}")                        #Inputing the user data path for the driver
    options.add_argument("--profile-directory=Default")                     #Specifing the profile directory
    options.add_argument(f"--user-agent={UserAgent().random}")
    options.binary_location = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'

    #DRIVER SETUP
    driver = webdriver.Chrome(service=Service(executable_path="C:\Selenium\chromedriver-win64\chromedriver.exe"), options=options)                      #Specifing the driver with the chromedriver path
    driver.implicitly_wait(30)                      #Wait 60 seconds for every action if it wasn't available at the moment

    phone = '01003816322'
    driver.get('https://web.whatsapp.com/send?phone=+2text=')

    msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msgBox.send_keys('السلام عليكم و رحمة الله و بركاته، أنا رسالة تلقائية')
    msgBox.send_keys(Keys.RETURN)
    print(f"message sent to {phone}")
    
    msgBox.send_keys(Keys.LEFT_CONTROL + 'v')
    videobox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')
    videobox.send_keys(Keys.RETURN)
    
    phone = '01111095963'
    driver.get('https://web.whatsapp.com/send?phone=+2' + phone + '&text=')

    msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msgBox.send_keys('السلام عليكم و رحمة الله و بركاته، أنا رسالة تلقائية')
    msgBox.send_keys(Keys.RETURN)
    print(f"message sent to {phone}")
    
    msgBox.send_keys(Keys.LEFT_CONTROL + 'v')
    videobox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')
    videobox.send_keys(Keys.RETURN)
   
    phone = '01147209471'
    driver.get('https://web.whatsapp.com/send?phone=+2' + phone + '&text=')

    msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msgBox.send_keys('السلام عليكم و رحمة الله و بركاته، أنا رسالة تلقائية')
    msgBox.send_keys(Keys.RETURN)
    print(f"message sent to {phone}")

    msgBox.send_keys(Keys.LEFT_CONTROL + 'v')
    videobox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')
    videobox.send_keys(Keys.RETURN)
    
def filecopy():
    import clr
    clr.AddReference('System.Collections.Specialized')
    clr.AddReference('System.Windows.Forms')
    from System.Collections.Specialized import StringCollection
    from System.Windows.Forms import Clipboard

    def main():

        files = StringCollection()
        file_path = 'D:\\$$$$\\Bots\\Whatsapp bot\\The Green City\\5 (2).mp4'
        files.Add(file_path)
        file_path = 'D:\\$$$$\\Bots\\Whatsapp bot\\The Green City\\Testimonial 1.mp4'
        files.Add(file_path)
        file_path = 'D:\\$$$$\\Bots\\Whatsapp bot\\The Green City\\Testimonial 2.mp4'
        files.Add(file_path)

        Clipboard.SetFileDropList(files)
    
    main()

def test4():

    n = 3

    for i in reversed(range(n)):
        print(5 - i, end=" ")

def divcountCheckloginSentcheckPyautogui():

    def main():

        attach_n = get_int("\n\nHow many attachements you want to send: ")

        #OPTIONS SETUP
        options = Options()                     #Defining options for the driver
        options.add_experimental_option("detach", True)                     #Force the browser to stay open even after fininshing
        user_data_dir = r'C:\Users\ideapad\AppData\Local\Google\Chrome Dev\User Data'                       #Path for user data
        options.add_argument(f"--user-data-dir={user_data_dir}")                        #Inputing the user data path for the driver
        options.add_argument("--profile-directory=Default")                     #Specifing the profile directory

        #DRIVER SETUP
        driver = webdriver.Chrome(service=Service(executable_path="C:\Selenium\chromedriver-win64\chromedriver.exe"), options=options)                      #Specifing the driver with the chromedriver path
        driver.implicitly_wait(30)                      #Wait 30 seconds for every action if it wasn't available at the moment
                

        while True:
            driver.get(f'https:/web.whatsapp.com/send?phone=+201003816322&text=')
            order = 0
            #Send first message
            msg = 'السلام عليكم و رحمة الله و بركاته'
            sendmsg(driver, msg)
            order += 1
            print(f"\n\nmessage nu.{order} is sent\n\n")

            #Send second message
            msg = 'السلام عليكم و رحمة الله و بركاته'
            sendmsg(driver, msg)
            order += 1
            print(f"\n\nmessage nu.{order} is sent\n\n")

                
    

    def checkLogin(driver, owner_phone):
        driver.get('https://web.whatsapp.com')
        try:
            link_with_phone = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.landing-window > div.landing-main > div > div > div._3rDmx > div > span').click()
        except NoSuchElementException:
            return True
        type_phone_number = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div/div/form/input')
        type_phone_number.send_keys(owner_phone)
        type_phone_number.send_keys(Keys.RETURN)
        code = ''
        for i in range(1, 8):
            code = code + driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[{i}]/span').text
        code = code + driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[8]/span').text
        return code

                        
    main()

def pyautogui():
    import pyautogui, sys

    # print('Press Ctrl-C to quit.')
    # try:
    #     while True:
    #         x, y = pyautogui.position()
    #         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #         print(positionStr, end='')
    #         print('\b' * len(positionStr), end='', flush=True)
    # except KeyboardInterrupt:
    #     print('\n')

    # pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
    # pyautogui.moveTo(700, 700, 2, pyautogui.easeOutQuad)    # start fast, end slow
    # pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
    # pyautogui.moveTo(700, 700, 2, pyautogui.easeInBounce)   # bounce at the end
    # pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end
    pyautogui

def commontest():
    import common
    from selenium.webdriver.common.by import By

    driver = common.driver_setup()
    driver.get("https://pamylka.com")

    test = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[8]/span')

def pandaLearn():
    conn = cm.conndb('whatsapp_bot')
    crsr = conn.cursor()

    df = pd.read_sql('select top 5 msg from msgs order by msg_order desc', conn)
    print(df)
    msg = df.iloc[-1]['msg']
    print(msg)
    driver = cm.driver_setup()
    driver.get("https://web.whatsapp.com/send?phone=+201003816322&text=")
    msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msgBox.send_keys(msg)
    msgBox.send_keys(Keys.RETURN)

def notification():
    noti = ToastNotifier()
    noti.show_toast("Hi, I'm title", "Hi, I'm the message", duration=3)

    msg = pag.alert(text='message', timeout=3000)

def negcount():
    count = -1
    count -= 1
    print(count)

def rangetest():
    for i in range(3):
        print(i)
    for i in range(1, 3):
        print(i)

def truefalse():
    if not is_vip('00000000', '010'):
        print('normal')
    else:
        print('vip')

def stringpiece():
    phone = '01003816322'
    print(phone[0:3])
    print(phone[3:])

def tmpdict():
    tmpmsgs = {}

    print(tmpmsgs)

    for i in range(5):
        tmpmsgs[i] = f"Hi, I'm {i}" 

    tmpmsgs['hi'] = 'hello'
    print(tmpmsgs['hi'])  

def setupexe():
    import sys
    from cx_Freeze import setup, Executable

    # Dependencies are automatically detected, but it might need fine tuning.
    build_exe_options = {
        "excludes": ["tkinter", "unittest"],
        "zip_include_packages": ["encodings", "PySide6"],
    }

    # base="Win32GUI" should be used only for Windows GUI app
    base = "Win32GUI" if sys.platform == "win32" else None

    setup(
        name="WhatBot",
        version="0.1",
        description="My GUI application!",
        options={"build_exe": build_exe_options},
        executables=[Executable("WHATBOT.py", base=base)],
    )

def useragent():
    driver = cm.driver_setup()
    driver.get("https://google.com")
    driver.get("https://web.whatsapp.com")
    driver.maximize_window()
    sleep(20)
    driver.close()

def ramainder():
    x = 120 % 100
    print(x)

def errorraise():
    class CanNotSendAttachements(BaseException): ...
    
    raise CanNotSendAttachements("Attachements can not be sent to 0100393499")

def waittest():
    driver = cm.driver_setup()
    driver.get("https://web.whatsapp.com/send?phone=+201003816322&text=")
    while True:
        try:
            link_with_phone = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.landing-window > div.landing-main > div > div > div._3rDmx > div > span').click()
            type_phone_number = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div/div/form/input')
            type_phone_number.send_keys('1555519931')
            type_phone_number.send_keys(Keys.RETURN)
            code = ''
            for i in range(1, 8):
                code = code + driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[{i}]/span').text + " - "
            code = code + driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[8]/span').text
            print(f"\n\nWhatsapp is logged out! \nPlease link the device using this code\n\n\t{code}\n *The bot will wait 1 min before generating another code")
            print("Whatsapp is logged out!", f"Please link the device using this code\n\n\t{code}\n *The bot will wait 1 min before generating another code")
            print("\n\n\nPlease login again\n\n\n")
            sleep(60)
        except NoSuchElementException:
            try:
                msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                msgBox.send_keys("Hi, I'm automated message")
                msgBox.send_keys(Keys.RETURN)
                print("\n\n\nNo login\n\n\n")
            except NoSuchElementException:
                pass
    print("\n\nSuccesfully logged in", "The BOT had logged into your whatsapp account succesfully\n\n")

def sendcheck():
    driver = cm.driver_setup()
    driver.get('https://web.whatsapp.com/send?phone=+201003816322&text=')

    while True:
        msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')

        msg = 'السلام عليكم و رحمة الله و بركاته أستاذة سارة أحمد مع حضرتك'
        msgBox.send_keys(msg)
        msgBox.send_keys(Keys.RETURN)

        #SEND second message
        msg = 'أستاذة سارة فوطة التراب اللى حضرتك كلمتينى عنها موجودة ان شاء الله و زى ماقولت لحضرتك الفوطة بتلمع الألوميتال أو أى حاجة متعبة بمرة واحدة بالمية بس، الفوطة بنبعتها لحضرتك تجربيها و لو مشتغلتش معاكى بترجعيها و فلوس الشحن و كل حاجة علينا'
        msgBox.send_keys(msg)
        msgBox.send_keys(Keys.RETURN)

        #COPY attachements
        files = StringCollection()
        for i in range(3):
            file_path = f'D:\\$$$$\\Bots\\Whatsapp bot\\The Green City\\{i}.mp4'
            files.Add(file_path)
        Clipboard.SetFileDropList(files)

        #SEND attachements
        msgBox.send_keys(Keys.LEFT_CONTROL + 'v')
        videobox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')
        videobox.send_keys(Keys.RETURN)
        
        #---IF ATTACHEMENTS ARE NOT SENT---#
        if not cm.sentcheck(driver):
            print("\n\n\nattachements are not sent\n\n\n")

        #---IF ATTACHEMENTS ARE SENT---#
        else:
            
            #NOTIFY me
            print(f"\n\n\nattachements are sent\n\n\n")
                
        #SEND last message
        msg = 'فشوفى حضرتك هتحتاجى كام واحدة منها و هستأذن حضرتك بس فى العنوان ابعت لحضرتك الأوردر ان شاء الله و لو فى أى حاجة انا تحت أمرك'
        msgBox.send_keys(msg)
        msgBox.send_keys(Keys.RETURN)

def shellexec():
    import subprocess
    
    sleep(10)
    subprocess.call(pag.hotkey('ctrl', 'c'), shell=True)

shellexec()