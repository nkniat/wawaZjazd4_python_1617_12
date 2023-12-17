import time
from selenium import webdriver

#inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"
new_url = "https://www.wp.pl"

# Otwarcie okna przeglądarki
driver.get(url)

# Sterowanie rozmiarem przeglądarki
driver.maximize_window()

# Otwarcie nowej zakładki
driver.execute_script("window.open('');")

# przełaczenie do okna
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)

# Zamyka daną zakładkę
driver.close()

time.sleep(15)

# Zakończ działanie przeglądarki
driver.quit()
