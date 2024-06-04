from selenium import webdriver                      #The webdriver to crawl the web
from selenium.webdriver.chrome.service import Service                       #Setup the executable path for the webdriver
from selenium.webdriver.chrome.options import Options                       #For more setup and specifications for the webdriver
from selenium.webdriver.common.by import By                     #To choose what selector to find element with
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pyodbc as odbc                       #Connect the app with sql
from fake_useragent import UserAgent



#---------------------CHECK IF THE USER LOGGED IN--------------------------#
#---------------------CHECK IF THE USER LOGGED IN--------------------------#

def loginCheck(driver, owner_phone, notifier):

        driver.get("https://web.whatsapp.com")
        try:
            link_with_phone = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.landing-window > div.landing-main > div > div > div._3rDmx > div > span').click()
            type_phone_number = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div/div/form/input')
            type_phone_number.send_keys(owner_phone)
            type_phone_number.send_keys(Keys.RETURN)
            code = ''
            for i in range(1, 8):
                code = code + driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[{i}]/span').text + " - "
            code = code + driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[8]/span').text
            print(f"\n\nWhatsapp is logged out! \nPlease link the device using this code\n\n\t{code}\n *The bot will wait 1 min before generating another code")
            notifier.show_toast("Whatsapp is logged out!", f"Please link the device using this code\n\n\t{code}\n *The bot will wait 1 min before generating another code", duration=6)
            sleep(60)
            loginCheck(driver, owner_phone, notifier)
        except NoSuchElementException:
            notifier.show_toast("Succesfully logged in", "The BOT had logged into your whatsapp account succesfully", duration=3)
            return True


#----------------------------------SETUP THE SELENIUM DRIVER------------------------------#
#----------------------------------SETUP THE SELENIUM DRIVER------------------------------#

def driver_setup(profile_dir='Default', path="C:\Selenium\chromedriver-win64\chromedriver.exe",  detach=True):
    #OPTIONS SETUP
    options = Options()                     #Defining options for the driver
    options.add_experimental_option("detach", detach)                     #Force the browser to stay open even after fininshing
    user_data_dir = r'C:\Users\ideapad\AppData\Local\Google\Chrome Dev\User Data'                       #Path for user data
    options.add_argument(f"--user-data-dir={user_data_dir}")                        #Inputing the user data path for the driver
    options.add_argument(f"--profile-directory={profile_dir}")                     #Specifing the profile directory
    options.add_argument(f"--user-agent={UserAgent().random}")
    
    #DRIVER SETUP
    driver = webdriver.Chrome(service=Service(executable_path=path), options=options)                      #Specifing the driver with the chromedriver path
    driver.implicitly_wait(30)
    

    return driver


#---------------------------CONNECT TO DATABASE----------------------------------#
#---------------------------CONNECT TO DATABASE----------------------------------#

def conndb(database, driver="ODBC Driver 17 for SQL Server", server='AHMED-ELBEHAIRY',  trstconn='yes'):
    conn = odbc.connect(f"Driver={driver};"          
        f"Server={server};"
        f"Database={database};"
        f"Trusted_Connection={trstconn};")                      #Making a pyodbc connection to the database
    return conn


#----------------------------CHECK IF THE MESSAGE IS SENT------------------------#
#----------------------------CHECK IF THE MESSAGE IS SENT------------------------#

def sentcheck(driver):

    if WebDriverWait(driver, 45).until(ec.any_of(
        ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=' Sent ']")),  ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=' Delivered ']")), ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=' Read ']")))
        ):
        return True
    return False


#----------------------FUNCTION FOR INSERTING MESSAGE TO DATABASE-------------------#
#----------------------FUNCTION FOR INSERTING MESSAGE TO DATABASE-------------------#

def insertMsg(crsr, msgs_table, starter, phone, msg, order, sender):
    crsr.execute(f"INSERT INTO {msgs_table} VALUES ('{starter + phone}', default, default, default, default, {order}, '{sender}', N'{msg}')")
    crsr.commit()


#---------------------------------NUMBER VALIDITY FUNCTION-------------------------#
#---------------------------------NUMBER VALIDITY FUNCTION-------------------------#

def numberValidity(driver):
    sleep(5)
    try:
        for i in range(10):
            try:
                validbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                return True
            except NoSuchElementException or UnexpectedAlertPresentException:
                try:
                    invalidbutton = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button')
                    return False
                except NoSuchElementException or UnexpectedAlertPresentException:
                    pass
    except UnexpectedAlertPresentException:
        pass
        