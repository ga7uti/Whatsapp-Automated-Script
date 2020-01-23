  
from selenium import webdriver

driver = webdriver.Chrome('/home/gauti/Desktop/Projects/python/pywhatsapp/chromedriver')
driver.get('http://web.whatsapp.com')

name = raw_input('Enter the name of user or group : ')
msg = raw_input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
raw_input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
print(user)
user.click()

#msg_box = driver.find_element_by_class_name('input-container')
msg_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
print(msg_box)
i=0
for i in range(count):
    print("Sending...")
    msg_box.send_keys(msg)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
    print("Sent...")
