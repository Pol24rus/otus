import os

import pytest

from gener_params import (
    gen_users
)
from my_store_api_user import MyStoreApiUser

# входные файлы для работы с тестами
USERS_FILE_NAME = os.getenv('USERS_FILE_NAME', 'users.csv')
USERS_ERROR_FILE_NAME = os.getenv('USERS_ERROR_FILE_NAME', 'users_error.csv')


@pytest.fixture(scope='function')
def my_store_api_user():
    return MyStoreApiUser()


#   генерация 2-х пользователей
@pytest.mark.parametrize('data', gen_users(2))
def test_create_user(my_store_api_user, data):  # принимаются данные
    user_id = my_store_api_user.create_user(**data)  # распаковываются данные, создаем пользователя
    assert user_id  # получаем ID пользователя

    # формируем ожидаемое тело
    expected_body = {
        **data,
        'id': user_id,
    }
    # проверяем по имени пользователя
    user_info = my_store_api_user.get('user', data['username'])
    # проверяем соответствие полученной инфы к ожидаемой
    for key, value in expected_body.items():
        assert user_info[key] == value, (
            f'[{key}] Actual value: {user_info[key]}, expected: {value}'
        )
# пользователей получаем из генератора den_params
