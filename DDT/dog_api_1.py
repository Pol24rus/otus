import os
import pytest
from test_request import BaseRequest, BASE_URL_DOGSTORE, BASE_URL_BREWERIES, BASE_URL_JSONPLACEHOLD


@pytest.fixture(scope='function') # получаю урл
def url_dogstore(dog_url):
    assert dog_url == "--expected: 'https://dog.ceo/api/breeds/image/random'"
    return BaseRequest(BASE_URL_DOGSTORE)

# какая ф-ция верная, dog_url или url_breweries в плане использования assert?
@pytest.fixture(scope='function') # получаю статус кода
def url_breweries(breweries_status):
    assert breweries_status == 200
    return BaseRequest(BASE_URL_BREWERIES)


@pytest.fixture(scope='function')
def url_jsonplacehold(jsonplacehold_url):
    return BaseRequest(BASE_URL_JSONPLACEHOLD)


