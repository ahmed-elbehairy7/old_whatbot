# |-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-| 
# RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPO 
# NDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER 
# RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPO 
# NDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER  
# RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPO 
#                                                                            RESPONDER RESPONDER RESPONDER  
#                                                                           ONDER RESPONDER RESPONDER RESPO 
#                                                                            RESPONDER RESPONDER RESPONDER  
#                                                                           ONDER RESPONDER RESPONDER RESPO
# Created by: AHMED ELBEHAIRY                                                RESPONDER RESPONDER RESPONDER 
# Date created: September 21 2023;                                          ONDER RESPONDER RESPONDER RESPO
# You can find the product at: https://shop.pamylka.com/whatbot              RESPONDER RESPONDER RESPONDER  
#                                                                           ONDER RESPONDER RESPONDER RESPO 
#                                                                            RESPONDER RESPONDER RESPONDER  
#                                                                           ONDER RESPONDER RESPONDER RESPO 
#                                                                            RESPONDER RESPONDER RESPONDER  
# RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPO 
# NDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER 
# RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPO 
# NDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER  
# RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPONDER RESPO 
# |-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-|-('-')-| 



from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
import pandas as pd
import pyodbc as odbc
import common as cm
import re
from win10toast import ToastNotifier
from details import Responder


#----------------------------------RESPOND FUNCTION----------------------------#
#----------------------------------RESPOND FUNCTION----------------------------#

def respond(conn, crsr, driver):

    print("\n\n\n|-('-')-|\t\tWELCOME TO THE RESPONDER - VERSION: 0.10.0\t\t|-('-')-|\n\n|-('-')-|\t\t\tBest Wishes for your Business\t\t\t|-('-')-|\n\n\n")

    #NOTIFIER SETUP
    notifier = ToastNotifier()
    notifier.show_toast("RESPONDING NOW!", "The RESPONDER is initiated", duration=3)
    
    #GET 
    phone_nums = pd.read_sql("select * from last_msgs where end_chat = 'NO'", conn)                     #Pandas read the sql table
    #HOW many client to respond
    msgs_count = pd.read_sql('exec msgs_count', conn).iloc[1]['count']
    count_r = pd.read_sql('exec resp_count', conn)
    count = 0


    #--------------------RESPONDING--------------------#

    for i in range(1, msgs_count + 1):
        #Getting the values of the number
        phone = phone_nums.iloc[i]['phone']                        #Defining phone as the last phone number messaged
        last_msg_recorded = phone_nums.iloc[i]['last_msg']

        EEfsh_Metkarar = set()

        #CHECK if you're logged in
        cm.loginCheck(driver, '1555519931', notifier, f'web.whatsapp.com/send?phone=+2{phone}&text=')

        #CHECK IF NUMBER AVAILABLE
        if not cm.numberValidity(driver):
            crsr.execute(f"insert into changed_nums values ('{phone}', 'VALID', 'INVALID')")
            continue

        #Getting the last msg in chat
        last_msg_in_chat = driver.find_element(By.CSS_SELECTOR, '#main > div._3B19s > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-last-child(1) > div > div > div > div._1BOF7._2AOIt > div:nth-child(2) > div > div.copyable-text > div > span._11JPr.selectable-text.copyable-text > span').get_attribute('innerHTML')

        #MAKE sure client responded
        if last_msg_in_chat == last_msg_recorded:
            continue

        last_msgs_count = 1

        #KNOWING where is the first message sent by the client
        while last_msg_in_chat != last_msg_recorded:
            last_msgs_count += 1
            last_msg_in_chat = driver.find_element(By.CSS_SELECTOR, f'#main > div._3B19s > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-last-child({last_msgs_count}) > div > div > div > div._1BOF7._2AOIt > div:nth-child(2) > div > div.copyable-text > div > span._11JPr.selectable-text.copyable-text > span').get_attribute('innerHTML')
        
        #Getting the order of the last message to start from
        order = pd.read_sql("select max(msg_order) as order_ from msgs where phone = '01000010312'").iloc[1]['order_']
        #Responding to messages one by one
        while last_msgs_count > 1:
            last_msgs_count -= 1
            order += 1
            tmporder = 0

            #GET the message we will respond to
            client_msg = driver.find_element(By.CSS_SELECTOR, f'#main > div._3B19s > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-last-child({last_msgs_count}) > div > div > div > div._1BOF7._2AOIt > div:nth-child(2) > div > div.copyable-text > div > span._11JPr.selectable-text.copyable-text > span').get_attribute('innerHTML')
            cm.insertMsg(crsr, 'msgs', phone[0:3], phone[3:], client_msg, order, 'CLIENT')

            #Determine the response details
            msg_responses = pd.read_sql(f"""if not exists (select msg from resp where N'{client_msg}' like msg)
begin 
insert into resp values (N'{client_msg}', 'noresp')
select count(response) as count from resp where N'{client_msg}' like msg and response <> 'noresp'
end
else 
begin
select count(response) as count from resp where N'{client_msg}' like msg and response <> 'noresp'
end""", conn).iloc[1]['count']
            
            #Defining the message box
            msgBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')

            #IF THERE'S NO RESPONSE SET YET
            if msg_responses == 0:
                continue

            response = pd.read_sql(f"""select response from resp where N'{client_msg} like msg and response <> 'noresp' """, conn)
            
            tmpmsgs = {}


            if msg_responses == 1:
                res = response.iloc[1]['response']
                if res in EEfsh_Metkarar:
                        continue
                end = response.iloc[i]['end_chat']
                msgBox.send_keys(res)
                msgBox.send_keys(Keys.RETURN)
                EEfsh_Metkarar.add(res)
                crsr.execute(f"update last_msgs set last_msg = N'{res}' end_chat = '{end}' where phone = '{phone}'")
                tmporder += 1
                tmpmsgs[tmporder] = res
          
            else:
                for i in range(1, msg_responses + 1):
                    res = response.iloc[i]['response']
                    if res in EEfsh_Metkarar:
                        continue
                    end = response.iloc[i]['end_chat']
                    msgBox.send_keys(res)
                    msgBox.send_keys(Keys.RETURN)
                    EEfsh_Metkarar.add(res)
                    crsr.execute(f"update last_msgs set last_msg = N'{res}' end_chat = '{end}' where phone = '{phone}'")
                    tmporder += 1
                    tmpmsgs[tmporder] = res

        for i in tmporder:
            crsr.execute(f"""INSERT INTO msgs VALUES ('{phone}', default, default, default, default, {tmporder + order}, 'BOT', N'{tmpmsgs[tmporder]})""")

    print("\n\n\n|-('-')-|\t\tGOODBYES FROM THE RESPONDER\t\t|-('-')-|\n\n\n")

def main():
    driver = cm.driver_setup()
    conn = cm.conndb('whatsapp_bot')
    crsr = conn.cursor()
    respond(conn, crsr, driver)


main()