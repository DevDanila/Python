from multiprocessing.sharedctypes import Value
import time
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('img')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
