from bases_request import BaseRequest, BASE_URL_DOGSTORE


class MyStoreApiUser(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_DOGSTORE)

    # базовый метод создания пользователя
    def create_user(  # принимает параметры для создания пользователей
            self, username, firstName, lastName, email,
            password, phone, userStatus, id=0, expected_error=False,
    ):
        data = {  # заполняет необходимые данные для создания пользователя
            "id": id,
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": userStatus
        }
        return self.post(
            'user', '', data, is_json=True, expected_error=expected_error
        )
