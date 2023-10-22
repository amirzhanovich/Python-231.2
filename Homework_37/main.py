from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument('--window-size=1920,1200')

driver = webdriver.Chrome(options=options)
driver.get('http://www.finmarket.ru/currency/rates/?id=10123')

def function(link):
    linkToTitle = link.find_elements(By.CLASS_NAME, 'title')
    for elem in linkToTitle:
        title = elem.text

    linkToValue = link.find_elements(By.CLASS_NAME, 'value')
    for elem in linkToValue:
        value = elem.text

    print(f'курс {title} к тенге = {value}')

USD = driver.find_element(By.ID, 'ft_52148')
EUR = driver.find_element(By.ID, 'ft_52170')
GBP = driver.find_element(By.ID, 'ft_52146')
CHF = driver.find_element(By.ID, 'ft_52133')

function(USD)
function(EUR)
function(GBP)
function(CHF)

driver.quit()