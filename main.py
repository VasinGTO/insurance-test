import json
from urllib.request import urlopen
import random

url_makers = 'https://api.tinkoff.ru/insurance-app/vehicle01/registry/'

makers_raw = json.loads(urlopen(url_makers).read().decode())
makers = makers_raw['payload']['makers']
# url = url + tree[0]['id'] + '/'

# print(tree[0]['id'])

for maker in random.sample(makers, 5):
    url_models = url_makers + maker['id'] + '/'
    models_raw = json.loads(urlopen(url_models).read().decode())
    models = models_raw['payload']['models']

    for model in models:
        url_years = url_models + model['id'] + '/'
        years_raw = json.loads(urlopen(url_years).read().decode())
        years =  years_raw['payload']['years']

        for year in random.sample(years,1):
            url_ages = url_years + str(year) + '/'
            # ages_raw = json.loads(urlopen(url_ages).read().decode())

            for age in random.sample(range(18,71),1):
                for exp in random.sample(range(0,min(age-18,30)+1),1):
                    url_premium = url_ages + str(age) + '/' + str(exp)
                    premium_raw = json.loads(urlopen(url_premium).read().decode())
                    try:
                        print(premium_raw['payload']['premium']['value'], premium_raw['status'])
                    except:
                        print(url_premium)
