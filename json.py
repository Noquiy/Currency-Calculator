import requests

requestDollar = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/")
requestEuro = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
requestPound = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/gbp/")

eur = requestEuro.json()
usd = requestDollar.json()
gbp = requestPound.json()

euroRate = eur['rates'][0]['mid']
dollarRate = usd['rates'][0]['mid']
poundRate = gbp['rates'][0]['mid']