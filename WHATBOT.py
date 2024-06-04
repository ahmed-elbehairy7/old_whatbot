# |-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-| 
# WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT 
# BOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHAT
# WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT WHATBOT 
# |-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-| 



from selenium.webdriver.common.by import By                     #To choose what selector to find element with
from selenium.webdriver.common.keys import Keys                     #To send keys like Enter and Ctrl
from selenium.common.exceptions import NoSuchElementException                       #To alert us that the element is not found
import pandas as pd                     #To read the data in database
from cs50 import get_int                        #To collect data from user before starting the bot
from time import sleep
from win10toast import ToastNotifier
from wakepy import keep

#Clr
import clr                      #CLR from pythonnet is necessary to copy the files to clipboard
clr.AddReference('System.Collections.Specialized')
clr.AddReference('System.Windows.Forms')
from System.Collections.Specialized import StringCollection
from System.Windows.Forms import Clipboard

#My own files and liberaries
from vip import is_vip                      #Help determine the vip numbers and execlude it
import common as cm                     #Get common functions
from details import WHATBOT



#----------------------------------MAIN FUNCTION----------------------------#
#----------------------------------MAIN FUNCTION----------------------------#
def main():

    with keep.presenting() as k:


        print(f"\n\n\n|-('-')-|\t\tWELCOME TO {WHATBOT.__name__} - VERSION: {WHATBOT.__version__}\t\t|-('-')-|\n\n|-('-')-|\t\t  Best Wishes with your Business  \t\t|-('-')-|\n\n\n")


        #DEFINING VARIABLES
        notifier = ToastNotifier()                      #Defining a notifier
        reachouts = get_int("How many reachouts do you want?: ")                     #Get the number of reachouts the user want to make
        attach_n = get_int("How many attachements you want to send: ")                      #Get the number of attachements
        count = 0                       #Define count variable
        messaged = 0                        #Defining messaged numbers variable
        

        #DRIVER SETUP
        driver = cm.driver_setup()                      #Webdriver setup
    
        #DATABASE SETUP
        conn = cm.conndb('whatsapp_bot')                        #Connecting to a database
        crsr = conn.cursor()                        #Defining a cursor to execute code in the connected database
        
        #------------------------GETTING THE LAST MESSAGED NUMBER---------------------#   

        lastNum = pd.read_sql('exec getLastNum', conn)                     #Pandas read the sql table
        starter = lastNum.iloc[-1]['starter']                     #Determining the starter
        phone = '00011247'                       #Defining phone as the last phone number messaged

        notifier.show_toast("SENDING NOW!", "THE WHATBOT is initiated!", duration=3)

        #MAKE SURE I'M LOGGED IN
        cm.loginCheck(driver, '1555519931', notifier)

        #---------------------------------THE BOT-------------------------------------#
        while messaged < reachouts:

            #PRINT number 
            count += 1                      #Count the new number
            print(f"\n\n{count}\n\n")                        #Print the count till now

            #GET right phone and starter
            starter = nextStarter(starter, phone)                       #Change the starter if numbers are fininshed
            phone = nextPhone(phone)                        #Get to the next number

            #---------MAKE SURE NUMBER IS NOT VIP---------#
            if is_vip(phone, starter):                      #If the number is vip number:
                crsr.execute(f"INSERT INTO done_nums VALUES ('{starter + phone}', '{starter}', '{phone}', 'UNKNOWN', 'VIP', default, default, default, default)"                         #Insert the number into the done numbers table
                    f"INSERT INTO vip_nums VALUES ('{starter + phone}', '{starter}', '{phone}', 'UNKNOWN')")                        #Insert the number into the normal numbers table
                print("\nnumber is vip\n")
                crsr.commit()
                continue

            if phone == '00011607':     #TEMP TEMP TEMP TEMP
                continue
                
            
            #-------MAKE SURE NUMBER IS AVAILABLE------#
            driver.get(f'https://web.whatsapp.com/send?phone=+2{starter}{phone}&text=')
            if not cm.numberValidity(driver):                       #If number is not valid
                insertValues(crsr, 'done_nums', 'invalid_nums', 'norm_nums', starter, phone, 'INVALID', '---')                  #Insert the values into the database tables
                crsr.commit()
                print("\nNumber is not valid\n")
                continue
            
                
            #SETUP the order variable and getting the messages box
            order = 0
            msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
            insertValues(crsr, 'done_nums', 'valid_nums', 'norm_nums', starter, phone, 'VALID', '---')                      #Insert the values into the database tables

            #SEND first message
            msg = 'السلام عليكم و رحمة الله و بركاته أستاذة سارة أحمد مع حضرتك'
            msgBox.send_keys(msg)
            msgBox.send_keys(Keys.RETURN)
            order += 1
            cm.insertMsg(crsr, 'msgs', starter, phone, msg, order, 'BOT')
            print(f"message nu. {order} is sent to {starter}{phone} and inserted in database")

            #SEND second message
            msg = 'أستاذة سارة فوطة التراب اللى حضرتك كلمتينى عنها موجودة ان شاء الله و زى ماقولت لحضرتك الفوطة بتلمع الألوميتال أو أى حاجة متعبة بمرة واحدة بالمية بس، الفوطة بنبعتها لحضرتك تجربيها و لو مشتغلتش معاكى بترجعيها و فلوس الشحن و كل حاجة علينا'
            msgBox.send_keys(msg)
            msgBox.send_keys(Keys.RETURN)
            order += 1
            cm.insertMsg(crsr, 'msgs', starter, phone, msg, order, 'BOT')
            print(f"message nu. {order} is sent to {starter}{phone} and inserted in database")

            #INSERT the last message to last_msgs table
            crsr.execute(f"insert into last_msgs values ('{starter + phone}', N'{msg}', default, default, default, default, 'No')")
            crsr.commit()

            #COPY attachements
            files = StringCollection()
            for i in range(attach_n):
                file_path = f'D:\\$$$$\\Bots\\Whatsapp bot\\The Green City\\{i}.mp4'
                files.Add(file_path)
                order += 1
            Clipboard.SetFileDropList(files)

            #SEND attachements
            msgBox.send_keys(Keys.LEFT_CONTROL + 'v')
            videobox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')
            videobox.send_keys(Keys.RETURN)
            
            #---IF ATTACHEMENTS ARE NOT SENT---#
            if not cm.sentcheck(driver):
                
                #NOTIFY me
                notifier.show_toast("FAILED TO SEND ATTACHEMENTS", f"Failed to send attachements to {starter + phone}, Please check your internet connection and try again!")
                print(f"Attachements are not send to {starter}{phone}, please retry your internet connection\n")
                print(f"Due to an error occured, the program stoped working at the number {starter}{phone}\n")
                print(f"To avoid losing a client by sending repeated messages we added it to the messaged clients table\n")
                print(f"You can find the number ({starter}{phone}) in error_nums table")

                #INSERT the number into the error numbers table and end the program
                crsr.execute(f"INSERT INTO error_nums VALUES ('{starter + phone}', '{starter}', '{phone}', 'VALID', '---', default, default, default, default)")                        #Inserting the value in the error_nums table
                crsr.commit()
                messaged = reachouts

            #---IF ATTACHEMENTS ARE SENT---#
            else:
                
                #NOTIFY me
                print(f"attachements are sent to {starter}{phone}")
                messaged += 1
                print(f'\n\nmessaged: {messaged}\n\n')
            
            
            #INSERT the values of them into msgs table
            for i in reversed(range(attach_n)):
                cm.insertMsg(crsr, 'msgs', starter, phone, 'video attachement', order - attach_n, 'BOT')
            sleep(15)
                
            #SEND last message
            msg = 'فشوفى حضرتك هتحتاجى كام واحدة منها و هستأذن حضرتك بس فى العنوان ابعت لحضرتك الأوردر ان شاء الله و لو فى أى حاجة انا تحت أمرك'
            msgBox.send_keys(msg)
            msgBox.send_keys(Keys.RETURN)
            order += 1
            cm.insertMsg(crsr, 'msgs', starter, phone, msg, order, 'BOT')
            print(f"message nu. {order} is sent to {starter}{phone} and inserted in database")
            
            #INSERT the values into tables
            crsr.execute(f"insert into last_msgs values ('{starter + phone}', N'{msg}', default, default, default, default, 'No')")
            crsr.commit()
            sleep(10)
                    

        #------------------------CLOSE BOT---------------------#

        crsr.commit()                       #Save the data to the database after fininshing
        driver.close()                      #Closes the browser for the responding bot

        print("\n\n\n|-('-')-|\t\tGOODBYES FROM WHATBOT\t\t|-('-')-|\n\n\n")
        print(WHATBOT)

        notifier.show_toast("DONE!!!", "Congratulations, the bot session had just ended ('-')", duration=8)


#
#
#-----------------------------------END OF BOT-------------------------------------#
#-----------------------------------END OF BOT-------------------------------------#
#-----------------------------------END OF BOT-------------------------------------#
#-----------------------------------END OF BOT-------------------------------------#



#----------------------------------NEXT NUMBER FUNCTION----------------------------#
#----------------------------------NEXT NUMBER FUNCTION----------------------------#

def nextPhone(phone):
    if phone == '99999999':
        return '00000000'
    else:
        return str(int(phone) + 1).zfill(8)


#--------------------------------NEXT STARTER FUNCTION-----------------------------#
#--------------------------------NEXT STARTER FUNCTION-----------------------------#

def nextStarter(starter, phone):
    if phone == '99999999':
        if starter == '015':
            return '010'
        elif starter == '012':
            return '015'
        else:
            return str(int(starter) + 1).zfill(3)
    return starter
        

#---------------------------------INSERT VALUES FUNCTION---------------------------#
#---------------------------------INSERT VALUES FUNCTION---------------------------#

def insertValues(cursor, done_table, validity_table, vip_table, starter, phone, validity, vip):
    cursor.execute(f"INSERT INTO {done_table} VALUES ('{starter + phone}', '{starter}', '{phone}', '{validity}', '{vip}', default, default, default, default)"                         #Insert the number into the done numbers table
                f"INSERT INTO {validity_table} VALUES ('{starter + phone}', '{starter}', '{phone}', '{vip}')"                        #Insert the number into the validity numbers tables
                f"INSERT INTO {vip_table} VALUES ('{starter + phone}', '{starter}', '{phone}', '{validity}')")                       #Insert the number into the vip numbers tables
    cursor.commit()


main()