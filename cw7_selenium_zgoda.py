import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# Otwarcie okna przeglądarki
url = "https://www.google.com"
driver.get(url)

# Sterowanie rozmiarem przeglądarki
driver.maximize_window()

# znajdz element 'akceptuj zgody' za pomocom xpath
accept = driver.find_element('xpath', '//*[@id="L2AGLb"]/div')
accept.click()

# znajdz pole do wpisania hasła 'pogoda'
search_box = driver.find_element('id', 'APjFqb')
search_box.send_keys('pogoda')

# nacisniecie Enter
search_box.send_keys(Keys.ENTER)

time.sleep(50)
# Zakończ działanie przeglądarki
driver.quit()