from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for=\"robotCheckbox\"]")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[for=\"robotsRule\"]")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:
    time.sleep(5)
    browser.quit()

