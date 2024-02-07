import pprint
import requests
import json

BASE_URL_DOGSTORE = 'https://dog.ceo/api/breed/hound/images'

response = requests.get(f'{BASE_URL_DOGSTORE}')
pprint.pprint('GET Example')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint(response.json())
pprint.pprint('*' * 20)

pass
data = {"message": "https:\\/\\/images.dog.ceo\\/breeds\\/retriever-flatcoated\\/n02099267_1018.jpg"}
response = requests.post(f'{BASE_URL_DOGSTORE}', data=data)

pprint.pprint('POST Example')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint('*' * 20)