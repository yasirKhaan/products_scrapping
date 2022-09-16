from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

DRIVER_PATH = '/home/yasirkhan/evaluation_dviz/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.analog.com/en/products.html')
# driver.get('https://www.analog.com/en/product-category/industrial-ethernet.html')

# for each_product in range(1, 19):
#     try:
#         xpath_string = "//body//div[@class='content']//div//div[2]//div//div//div//div//div//ul//li["+str(each_product)+"]//a"
#         products = driver.find_element(By.XPATH, xpath_string)
#         print((products.text))
#     except:
#         break

#     products = driver.find_element(By.XPATH, xpath_string)

# xpath_string = "/html/body/div[5]/div[1]/div[2]/div/div/div/div/div/ul"

# for i in range(1,1000):
#     products = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/div/div/div/ul/li['+str(i)+']')
#     print(len(products.text))

# print((products.text))
# print(len(products.get_attribute('')))




            



# product_xpath_string = "/html/body/div[5]/div[1]/div[2]/div/div/div/div/div/ul"

# product_xpath_string = "//body//div[5]//div//div[2]//div//div//div//div//div//ul"

# products = driver.find_element(By.XPATH, product_xpath_string)
# print(products.text, " DONE")
# sub_products_link = products.get_attribute('href')
# driver.get(sub_products_link)

# for each_category in range(1, 2):
#     try:
#         # xpath_string = "/html/body/div[5]/div[1]/div[3]/div/div/div/div/div"

#         xpath_string = '/html/body/div[5]/div[1]/div[2]/div/div/div/div/div/ul/li'
#         sub_products = driver.find_element(By.XPATH, xpath_string)
#         print(("Sub-Categ --> ", sub_products.text))
#     except:
#         pass


# time.sleep(5)
# driver.back()



def main():
    for each_product in range(1, 17):
        product_xpath_string = "//body//div[@class='content']//div//div[2]//div//div//div//div//div//ul//li["+str(each_product)+"]//a"
        products = driver.find_element(By.XPATH, product_xpath_string)
        print(products.text, " DONE")
        sub_products_link = products.get_attribute('href')
        driver.get(sub_products_link)

        for each_category in range(1, 50):
            try:
                xpath_string = "//body//div[@class='content']//div//div[2]//div//div//div//div//div//ul//li["+str(each_category)+"]//a"
                sub_products = driver.find_element(By.XPATH, xpath_string)
                print(("Sub-Categ --> ", sub_products.text))
            except:
                pass


        time.sleep(5)
        driver.back()
main()