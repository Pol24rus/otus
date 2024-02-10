import pprint
import requests
import json

# для 1-го сайта с полным адресом https://dog.ceo/api/breeds/image/random
BASE_URL_DOGSTORE = 'https://dog.ceo/api/breeds'
# для 2-го сайта с полным адресом https://api.openbrewerydb.org/v1/breweries
BASE_URL_BREWERIES = 'https://api.openbrewerydb.org/v1/breweries'
# для 3-го сайта с адресом https://jsonplaceholder.typicode.com/
BASE_URL_JSONPLACEHOLD = 'https://jsonplaceholder.typicode.com'


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

# присваиваю переменным значения урл
response_dog = requests.get(f'{BASE_URL_DOGSTORE}/image/random')
response_breweries = requests.get(f'{BASE_URL_BREWERIES}/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')
response_jsonplacehold = requests.get(f'{BASE_URL_JSONPLACEHOLD}/posts/1')
pprint.pprint('GET Example')

dog_url = response_dog.url  # буду сверять урл, поэтому создал переменную
print('dog_url', dog_url)
pprint.pprint(response_dog.headers)
pprint.pprint(response_dog.status_code)
pprint.pprint(response_dog.reason)
pprint.pprint(response_dog.text)
pprint.pprint(response_dog.json())
pprint.pprint('*' * 20)

breweries_url = response_breweries.url
print('breweries_url', breweries_url)
breweries_status = response_breweries.status_code
print('breweries_status = ', breweries_status)
# pprint.pprint(response_breweries.url)
pprint.pprint(response_breweries.status_code)
pprint.pprint(response_breweries.reason)
pprint.pprint(response_breweries.text)
pprint.pprint(response_breweries.json())
pprint.pprint('/' * 20)

jsonplacehold_url = response_jsonplacehold.url
print('jsonplacehold_url', jsonplacehold_url)
# pprint.pprint(response_jsonplacehold.url)
pprint.pprint(response_jsonplacehold.status_code)
pprint.pprint(response_jsonplacehold.reason)
pprint.pprint(response_jsonplacehold.text)
pprint.pprint(response_jsonplacehold.json())
pprint.pprint('-' * 20)

pass
# data = {"message": "https:\\/\\/images.dog.ceo\\/breeds\\/retriever-flatcoated\\/n02099267_1018.jpg"}
# response = requests.post(f'{BASE_URL_DOGSTORE}', data=data)

# pprint.pprint('POST Example')
#
# pprint.pprint(response.status_code)
# pprint.pprint(response.reason)
# pprint.pprint('*' * 20)
