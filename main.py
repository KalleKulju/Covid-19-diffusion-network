import requests
import json
from matplotlib import pyplot as plt

url = 'https://sampo.thl.fi/pivot/prod/fi/epirapo/covid19case/fact_epirapo_covid19case.json?column=dateweek20200101-509030L'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response_API = requests.get(url, headers=headers)


data = response_API.text
dataJS = json.loads(data)

tartuntamaarat = []
tervehtyneet = [0, 0]
x = 0
for viikko in range(len(dataJS['dataset']['value']) - 1):
    tartuntamaarat.append(int(dataJS['dataset']['value'][str(viikko)]))
    tervehtyneet.append(int(dataJS['dataset']['value'][str(viikko)]))

del tervehtyneet[-2:]


viikkojen_tartuntamaarat_yhteensa = []
viikkojen_tervehtyneet_yhteensa = []

for viikko in range(len(tartuntamaarat) + 1):
    summa = 0
    for x in range(viikko):
        summa += int(tartuntamaarat[x])
    viikkojen_tartuntamaarat_yhteensa.append(summa)

for viikko in range(len(tartuntamaarat) + 1):
    summa = 0
    for x in range(viikko - 2):
        summa += int(tartuntamaarat[x])
    viikkojen_tervehtyneet_yhteensa.append(summa)

print(viikkojen_tervehtyneet_yhteensa)
plt.plot(tartuntamaarat)
plt.plot(tervehtyneet)
plt.show()
