from selenium import webdriver
from selenium.webdriver.common.by import By  #pomoc w lokalizacji elementów

import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/")

#driver.set_window_size(1000, 1000)
driver.maximize_window() #może wpływać na stabilność testów

accept = driver.find_element("id", "accept-choices")
accept.click()

menu = driver.find_element("id", "navbtn_tutorials").click()
#webdriver.ActionChains(driver).move_to_element(menu).perform()

# klikniecie
#webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# Learn HTML
HTMLTutorial = driver.find_element("xpath", '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
HTMLTutorial.click()

time.sleep(5) #dlugo sie laduje to menu
# HTML References >> Tag List
HTMLAtributes = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[67]')
HTMLAtributes.click()

# <input>
disabled = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/div/a[59]')
disabled.click()

# try it yourself
inputExample = driver.find_element('xpath', '//*[@id="main"]/div[3]/a')
inputExample.click()
print(driver.title)

currentWindow_name = driver.current_window_handle
windowNames = driver.window_handles

for window in windowNames:
    if window != currentWindow_name:
        driver.switch_to.window(window)

print(driver.title)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))

firstName = driver.find_element(By.ID, 'fname')

if firstName.is_enabled():
    firstName.send_keys('Natalia')
else:
    print('Nie da sie kliknac')

driver.close()

driver.switch_to.window(currentWindow_name)

print(driver.title)

driver.back()
driver.back()

time.sleep(10)

# HTML Forms >> Input Types
inputTypes = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')
inputTypes.click()

# Input Type Checkbox
tryCheckbox = driver.find_element('xpath', '//*[@id="main"]/div[13]/a')
tryCheckbox.click()

currentWindow_name = driver.current_window_handle
windowNames = driver.window_handles

for window in windowNames:
    if window != currentWindow_name:
        driver.switch_to.window(window)

print(driver.title)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))

bike = driver.find_element(By.ID, 'vehicle1')
bike.click()

time.sleep(10)


driver.close()
driver.switch_to.window(currentWindow_name)

time.sleep(500)

driver.quit()

