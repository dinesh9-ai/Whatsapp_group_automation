import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.support.ui import Select

def gadd(n):
    l=[]
    a=pd.read_csv('names.csv')
    for i in a['names']:
        l.append(i)
    d=webdriver.Chrome()
    q=d.get('https://web.whatsapp.com/')
    time.sleep(30)
     try:
        driver.find_element_by_xpath('//*[@title="{}"]'.format(n)).click()
    except:
        print('WhatsApp group is not there\n please try again')
    w=WebDriverWait(d,30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_3V5x5"]')))
    w.click()
    w=WebDriverWait(d,30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_3p0T6"]')))
    for i in l:
        d.find_element_by_xpath('//*[@title="Search…"]').send_keys(i)
        time.sleep(5)
        d.find_element_by_xpath('//*[@title="{}"]'.format(i)).click()
    d.find_element_by_xpath('//*[@data-icon="checkmark-light"]').click()
    time.sleep(5)
    w = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_2eK7W _3PQ7V"]')))
    w.click()
    return
gadd(input('enter group name'))
