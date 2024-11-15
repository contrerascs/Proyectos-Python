from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

df = pd.read_csv(r'Automate-Webs/fake_data.csv')

path = 'D:/Sam Contreras/Documents/Programacion/Python/ChromeDriver/chromedriver.exe'
service = Service(executable_path=path)
website = 'https://forms.gle/HfsmuhZbP3X2hGbTA'
driver = webdriver.Chrome(service=service)

for i in range(0,len(df)):
    driver.get(website)
    for columna in df.columns:
        texto_input = driver.find_element(by='xpath',
                                    value=f'//div[contains(@data-params, "{columna}")]//input | //div[contains(@data-params, "{columna}")]//textarea')

        texto_input.send_keys(df.loc[i,columna])

    button_enviar = driver.find_element(by='xpath', value='//div[@role="button"]//span[text()="Enviar"]')
    button_enviar.click()
    time.sleep(2)

time.sleep(2)
driver.quit()