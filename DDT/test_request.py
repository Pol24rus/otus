import pprint
import requests
import json

BASE_URL_DOGSTORE = 'https://dog.ceo/dog-api/documentation/random'
# BASE_URL_DOGSTORE = 'https://petstore.swagger.io/v2/pet/10'

response = requests.get(f'{BASE_URL_DOGSTORE}')
pprint.pprint('GET Example')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint(response.json())
pprint.pprint('*' * 20)

pass
