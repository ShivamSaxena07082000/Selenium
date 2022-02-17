from selenium import webdriver
import pandas as pd
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.amazon.in/")
Name=[]
Price=[]
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('Samsung')
driver.find_element_by_id("nav-search-submit-button").click()
phone_names=driver.find_elements_by_xpath("//span[contains(@class,'a-size-medium a-color-base a-text-normal')]]")
for i in phone_names:
    print(i.text)
    Name.append(i.text)
prices=driver.find_elements_by_xpath("//span[contains(@class,'a-price-whole')]")
for j in prices:
    print(j.text)
    Price.append(j.text)

data={'Phone Names':Name,'Prices':Price}
df=pd.DataFrame(data)
df.to_csv('C:\\Users\\PC\\Downloads\\Desktop\\Shivam1.csv')



