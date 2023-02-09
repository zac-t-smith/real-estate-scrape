import  requests
import pandas as pd



headers = {
    'authority': 'api.crexi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'client-timezone-offset': '-6',
    'content-type': 'application/json',
    'mixpanel-distinct-id': '1862d6e52cea24-037018e23174e7-26021051-144000-1862d6e52cf132c',
    'origin': 'https://www.crexi.com',
    'referer': 'https://www.crexi.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

data = '{"subtypes":["Apartment Building"],"types":["Multifamily"],"latitudeMax":null,"latitudeMin":null,"longitudeMax":null,"longitudeMin":null,"count":60,"mlScenario":"search-properties-challenger-a","offset":0,"userId":"1862d6e52cea24-037018e23174e7-26021051-144000-1862d6e52cf132c","sortDirection":"Descending","sortOrder":"rank","includeUnpriced":true,"excludeUnpriced":null}'

response = requests.post('https://api.crexi.com/assets/search', headers=headers, data=data)

result_json = response.json()
result_items = result_json['data']

# address
full_address = result_items[2]['locations'][0]['fullAddress']

# description
descript = result_items[2]['description']

# asking price
asking_price = result_items[2]['askingPrice']

address = []
description = []
askingPrice = []

for result in result_items:
    try:
        try:
            # address
            address.append(result['locations'][0]['fullAddress'])
        except:
            address.append('N/A')

        # description
        if 'description' in result:
            description.append(result['description'])
        else:
            description.append('Not available')

        # asking price
        if 'askingPrice' in result:
            askingPrice.append(result['askingPrice'])
        else:
            askingPrice.append('Not Available')
    except IndexError:
        # If an index error occurs, simply skip the current iteration
        pass
    
import pandas as pd
df = pd.DataFrame({'Address': address, 'Description': description, 'Asking Price': askingPrice})


address = []
description = []
askingPrice = []

for i in range(1,180):
    
    headers = {
    'authority': 'api.crexi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'client-timezone-offset': '-6',
    'content-type': 'application/json',
    'mixpanel-distinct-id': '1862d6e52cea24-037018e23174e7-26021051-144000-1862d6e52cf132c',
    'origin': 'https://www.crexi.com',
    'referer': 'https://www.crexi.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    data = '{"subtypes":["Apartment Building"],"types":["Multifamily"],"latitudeMax":null,"latitudeMin":null,"longitudeMax":null,"longitudeMin":null,"count":60,"mlScenario":"search-properties-challenger-a","offset":0,"userId":"1862d6e52cea24-037018e23174e7-26021051-144000-1862d6e52cf132c","sortDirection":"Descending","sortOrder":"rank","includeUnpriced":true,"excludeUnpriced":null}'
    
    response = requests.post('https://api.crexi.com/assets/search', headers=headers, data=data)

    result_json = response.json()
    result_items = result_json['data']
    
    for result in result_items:
        try:
            try:
                # address
                address.append(result['locations'][0]['fullAddress'])
            except:
                address.append('N/A')

        # description
            if 'description' in result:
                description.append(result['description'])
            else:
                description.append('Not available')

            # asking price
            if 'askingPrice' in result:
                askingPrice.append(result['askingPrice'])
            else:
                askingPrice.append('Not Available')
        except IndexError:
        # If an index error occurs, simply skip the current iteration
            pass
df = pd.DataFrame({'Address': address, 'Description': description, 'Asking Price': askingPrice})


df.to_excel('C:\\Users\\ZacTS\\.spyder-py3\\Genesis_Research.xlsx', index=False, sheet_name='Python Properties')