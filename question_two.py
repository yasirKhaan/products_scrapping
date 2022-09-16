from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

DRIVER_PATH = '/home/yasirkhan/evaluation_dviz/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.st.com/content/st_com/en.html')


product_xpath_string = "//*[@id='Top_Menu_Products']/div/div/div[1]/ul/div[2]/div"

product_xpath_string = "//body//div[@class='off-canvas-wrap']//div//header//nav//"


products = driver.find_element(By.XPATH, product_xpath_string)
print(products.text)