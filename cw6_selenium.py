import time
from selenium import webdriver

#inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# Otwarcie okna przeglądarki
driver.get("https://www.google.com")

time.sleep(5)

# Zakończ działanie przeglądarki
driver.quit()
