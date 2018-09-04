from selenium import webdriver
import logging as log
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
log.info('Welcome to Chrome')


driver= webdriver.Chrome(c.CHROME_DRIVER_PATH)

driver.get("https://web.whatsapp.com/")

name= 'Wiki'
msg= 'Hello World'
count= 2
input('Enter anything after QR code is scanned')

user= driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box= driver.find_element_by_class_name('_1Plpp')

for i in range(count):
    msg_box.send_keys(msg)
    send_btn= driver.find_element_by_class_name('_35EW6')
    send_btn.click()