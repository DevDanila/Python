from multiprocessing.sharedctypes import Value
from selenium import webdriver
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))


link ='http://suninjuly.github.io/explicit_wait2.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
   

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button2 = browser.find_element_by_id("book")
    button2.click()
   
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    
    button1 = browser.find_element_by_xpath("//button[text()='Submit']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
