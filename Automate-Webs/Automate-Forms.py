from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = 'D:/Sam Contreras/Documents/Programacion/Python/ChromeDriver/chromedriver.exe'
service = Service(executable_path=path)
website = 'https://forms.gle/eTNRu5UrdjYSvVrY9'
driver = webdriver.Chrome(service=service)