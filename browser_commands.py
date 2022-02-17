from selenium import webdriver
driver=webdriver.Chrome(executable_path="chromedriver.exe")
class testing():
    def func(self):
        driver.get("https://secure.yatra.com/")
        driver.find_element_by_link_text('Yatra for Business').click()
        d=driver.find_elements_by_tag_name('a')
        for i in d:
            print(d.text)

ob=testing()
ob.func()
