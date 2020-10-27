from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

def bookparking(skifield='whakapapa', num=3):
    # whakapapa / friday

    driver = webdriver.Chrome()
    driver.get("https://parking.evacheckin.com/car_park_booking/select_dates?siteId=2")

    # select ski field here

    try:
        if skifield == 'turoa':
            turoa = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/button[1]')[0]
            turoa.click()
        if skifield == 'whakapapa':
            whakapapa = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/button[2]')[0]
            whakapapa.click()
    except Exception:
        time.sleep(2)
        if skifield == 'turoa':
            turoa = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/button[1]')[0]
            turoa.click()
        if skifield == 'whakapapa':
            whakapapa = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/button[2]')[0]
            whakapapa.click()
            
            
    enter_booking = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/button[3]')[0]
    enter_booking.click()
    time.sleep(2)

    # select day
    # the last div[number]/button: replace number with: 1=wed, 2=thu, 3=fri, 4=sat etc.
    
    try:
        day = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[{num}]/button')[0]
    except Exception:
        time.sleep(2)
        day = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[{num}]/button')[0]
        
    day.click()

    try:
        tobook = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[2]/button')[0]
    except Exception:
        time.sleep(2)
        tobook = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[2]/button')[0]
        
    tobook.click()
    
    time.sleep(2)

    try:
        driver.find_element_by_id('FirstName').send_keys("Firstname")
    except Exception:
        print(f"no available slots {skifield} {num}")
        driver.close()
        return False

    driver.find_element_by_id('LastName').send_keys("Lastname")
    driver.find_element_by_id('Phone').send_keys("MyPhoneNumber")
    driver.find_element_by_id('Email').send_keys("ryelye@email.com")
    driver.find_element_by_id('Rego').send_keys("Carrego")
    final = driver.find_elements_by_xpath('//*[@id="ButtonEnterDetails"]')[0]
    final.click()
    time.sleep(2)
    final_submit = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/button')[0]
    final_submit.click()
    time.sleep(20)
    driver.close()

    return True

while True:
    bp = bookparking(skifield='turoa', num=2)
    if bp == True:
        print('success on turoa2')
        break
    time.sleep(3)