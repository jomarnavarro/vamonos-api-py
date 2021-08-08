import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(quote_res.text, 'html.parser')

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
payload={'api_key':'DEMO_KEY', 'sol':1000, 'page':1}
r = requests.get(url, params=payload)

[x['camera']['name'] for x in r.json()['photos'] ]
freqs = {}
for x in [x['camera']['name'] for x in r.json()['photos'] ]:
    if x in freqs:
            freqs[x] += 1
    else:
            freqs[x] = 1

for x in [x['camera']['name'] for x in r.json()['photos'] ]:
    if x in freqs:
            freqs[x] += 1
    else:
            freqs[x] = 1

freqs
{'FHAZ': 2, 'RHAZ': 2, 'MAST': 21}
first_ten = [x['camera']['name'] for x in r.json()['photos'] ][:11]
first_ten
first_ten = [x['camera']['name'] for x in r.json()['photos'] ][:10]
first_ten
['FHAZ', 'FHAZ', 'RHAZ', 'RHAZ', 'MAST', 'MAST', 'MAST', 'MAST', 'MAST', 'MAST']
freqs = {}
for x in first_ten:
    if x in freqs:
            freqs[x] += 1
    else:
            freqs[x] = 1

freqs
#{'FHAZ': 2, 'RHAZ': 2, 'MAST': 6}
freqs.values()
#dict_values([2, 2, 6])
list(freqs.values()).sort()
list(freqs.values()).sort()
val_list = list(freqs.values()).sort()
val_list
val_list = list(freqs.values())
val_list
#[2, 2, 6]
val_list.sort()
val_list
#[2, 2, 6]
#val_list = [4,3,6,3,8,1]
#val_list.sort()
#val_list
#[1, 3, 3, 4, 6, 8]
#times = val_list[-1]/val_list[0]
#times
#8.0