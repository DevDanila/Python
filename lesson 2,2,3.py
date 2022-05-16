from multiprocessing.sharedctypes import Value
import time
from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#num1')
    y_element = browser.find_element_by_css_selector('#num2')
    x = int(x_element.text)
    y = int(y_element.text)
    result = x + y
    result = str(result)
    select = Select(browser.find_element_by_css_selector('#dropdown'))
    select.select_by_visible_text(result)
   
    
  
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
