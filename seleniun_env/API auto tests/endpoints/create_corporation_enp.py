import requests
from endpoints.create_user_enp import CreateUserEndp

class CreateCorporationEnp(CreateUserEndp):
    code = None
    response_message = None
    response_corp_id = None
    payload = None

    # Метод на создание корпорации
    def create_corporation(self, auth, body):
        response = requests.post(url = 'https://api.brainy.run/go/create_corporation', auth = auth, json = body)
        self.code = response.status_code
        self.response_message = response.json()['message']
        self.response_corp_id = response.json()['corporation_id']
        self.payload = response.json()
        print(self.payload)
        return response
        
    # Проверка, что статус код 201
    def response_status_is_201(self):
        assert self.code == 201, f'Error [create_corporation_enp] status code = {self.code}, вместо 201'

    def response_message_is(self):
        assert self.response_message == 'Корпорация успешно создана', f'Error [create_corporation_enp] в теле сообщение {self.response_message}'

    def response_corp_id_body(self):
        assert type(self.response_corp_id) == int, f'Error [create_corporation_enp] в теле id корпорации не в видео инта'