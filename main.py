from datetime import datetime

import requests

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

requestDollar = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/")
requestEuro = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
requestPound = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/gbp/")

eur = requestEuro.json()
usd = requestDollar.json()
gbd = requestPound.json()

euroRate = eur['rates'][0]['mid']
dollarRate = usd['rates'][0]['mid']
poundRate = gbd['rates'][0]['mid']

print(euroRate, dollarRate, poundRate)
