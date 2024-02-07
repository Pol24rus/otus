import pprint
import requests

BASE_URL_DOGSTORE = 'https://dog.ceo/api/breeds/image/random'

class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
    # принимаем базовый урл чтобы не передавать везде потом
    # также можно данные авторизации и проч

    def _request(
            self, url, request_type, payload=None, is_json=False,
            expected_error=False
    ):
        pprint.pprint(f'Request to: {url}')
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                responce = requests.get(url)
            elif request_type == 'POST':
                if is_json:
                    responce = requests.post(url, json=payload)
                else:
                    responce = requests.post(url, data=payload)
            else:
                responce = requests.delete(url)

            if not expected_error and responce.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        pprint.pprint(f'{request_type} example')
        pprint.pprint(responce.url)
        pprint.pprint(responce.status_code)
        pprint.pprint(responce.reason)
        pprint.pprint(responce.text)
        pprint.pprint(responce.json())
        pprint.pprint('* ' * 20)
        return responce

