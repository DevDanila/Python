import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://suninjuly.github.io/math.html"

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(url)
    x = driver.find_element(By.ID, "input_value").text
    res_func = calc(x)
    res_input = driver.find_element(By.ID, "answer").send_keys(res_func)
    robot_in = driver.find_element(By.ID, "robotCheckbox").click()
    robot_rule = driver.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(2)

except Exception as ex:
    print(" *** Возникла ошибка *** ", ex)
finally:
    time.sleep(10)
    driver.quit()