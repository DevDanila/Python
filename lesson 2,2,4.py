from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    action1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    action1.click()
    
    action2 = browser.find_element_by_css_selector("[value='robots']")
    action2.click()
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()