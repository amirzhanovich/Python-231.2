import requests
from bs4 import BeautifulSoup

url = 'https://www.meteoprog.com/ru/weather/Astana/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
weather = soup.find('div', class_="today-temperature")
print("Погода в Астане на сегодня", weather.find('span').text)