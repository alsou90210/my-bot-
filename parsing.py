import requests 
import json 

API_ID = '4058e54826c44823a50b1b7a9fd078e7'

def exchager_currency():
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={API_ID}')

    data = json.loads(response.text)
    rates = data['rates']
    filter_rates = {
        'RUB':rates['RUB'],
        'KGS':rates['KGS'],
        'KZT':rates['KZT'],
        'TRY':rates['TRY'],
        'CNY':rates['CNY'],
        'AED':rates['AED'],
    }
    


    return filter_rates
exchager_currency()

