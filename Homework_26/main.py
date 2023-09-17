import requests
import json

url = 'https://www.cbr-xml-daily.ru/latest.js'
response = requests.get(url)
print(response.status_code)

with open('data.json', 'w') as file:
    json.dump(response.json(), file, indent=2)

data = response.json()
kzt = data['rates']['KZT']
usd = data['rates']['USD']
eur = data['rates']['EUR']
cny = data['rates']['CNY']

s = float(input("Введите сумму в тенге: "))
q = float(input("В какую валюту необходимо перевести тенге? Выбери один из: [1] USD, [2] EUR, [3] CNY\n"))
if (q==1):
    print(s/kzt*usd)
elif (q==2):
    print(s/kzt*eur)
elif (q==3):
    print(s/kzt*cny)
else:
    print("Выберите один из: [1] USD, [2] EUR, [3] CNY")





