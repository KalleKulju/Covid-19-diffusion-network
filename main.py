import requests
import json
from matplotlib import pyplot as plt
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep

#api for infections
url = 'https://sampo.thl.fi/pivot/prod/fi/epirapo/covid19case/fact_epirapo_covid19case.json?column=dateweek20200101-509030L'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response_API = requests.get(url, headers=headers)

data = response_API.text
dataJS = json.loads(data)

#api for deaths
url_deaths = 'https://sampo.thl.fi/pivot/prod/fi/epirapo/covid19case/fact_epirapo_covid19case.json?row=dateweek20200101-509030&column=measure-492118&fo=1'
response_API_deaths = requests.get(url_deaths, headers=headers)

data_deaths = response_API_deaths.text
dataJS_deaths = json.loads(data_deaths)

infection_amounts = []
recovered_amounts = [0, 0]
x = 0


death_amounts = []
x = 0

for week in range(len(dataJS_deaths['dataset']['value']) - 1):
    death_amounts.append(int(dataJS_deaths['dataset']['value'][str(week)]))


for week in range(len(dataJS['dataset']['value']) - 1):
    infection_amounts.append(int(dataJS['dataset']['value'][str(week)]))
    #deaths start at week 10 (index 9)
    if week < 9:
        recovered_amounts.append(int(dataJS['dataset']['value'][str(week)]))
    else:
        recovered_amounts.append(int(dataJS['dataset']['value'][str(week)]) - int(dataJS_deaths['dataset']['value'][str(week - 9)]))


del recovered_amounts[-2:]


weekly_infections_combined = []
weekly_recovered_combined = []

for week in range(len(infection_amounts) + 1):
    sum = 0
    for x in range(week):
        sum += int(infection_amounts[x])
    weekly_infections_combined.append(sum)

for week in range(len(infection_amounts) + 1):
    sum = 0
    for x in range(week - 2):
        sum += int(infection_amounts[x])
    weekly_recovered_combined.append(sum)

print(weekly_recovered_combined)
plt.plot(infection_amounts)
plt.plot(recovered_amounts)
plt.show()

#death amounts


weekly_dead_combined = []

for week in range(len(death_amounts) + 1):
    sum = 0
    for x in range(week):
        sum += int(death_amounts[x])
    weekly_dead_combined.append(sum)

print(weekly_dead_combined)
plt.plot(death_amounts)
plt.show()
