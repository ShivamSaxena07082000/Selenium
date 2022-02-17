from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://symptoms.webmd.com/")
age1=[]
age=driver.find_element_by_xpath('//*[@id="age"]')
age.send_keys('20')
driver.find_element_by_xpath('//*[@id="male"]/span').click()
a=driver.find_elements_by_xpath('//*[@id="male"]/span')
for i in a:
    print(i.text)
driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div[1]/div/div[2]/div/div/div[2]/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div[1]/div/div[3]/div[1]/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div[1]/div/div[3]/div[1]/div[1]/div[2]/input').send_keys('fev')
time.sleep(9)
driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/div[1]/label/span').click()
driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div[1]/div/div[3]/div[3]/div/div/button').click()
driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div[1]/div/div[3]/div[2]/button[2]').click()
time.sleep(3)
for i in range(1,3):
    question=driver.find_element_by_xpath("//h5[text()='Current medications']")
    print(question)


















