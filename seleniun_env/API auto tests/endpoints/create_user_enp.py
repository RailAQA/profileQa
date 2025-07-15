import requests
from faker import Faker

class CreateUserEndp:
    def create_user(self):
        
        fake_ru = Faker('ru_RU')
        fake_eng = Faker('en_EN')
        auth_brainy = ('a', "a")
        auth_body = {
  "avatar_url": "https://brainy.run/wp-content/uploads/2024/05/candidate2.png",
  "email": fake_ru.ascii_free_email(),
  "name": fake_ru.last_name_male(),
  "password": "superpassword",
  "role": "owner",
  "username": fake_eng.first_name()
}
        response_auth = requests.post(url = 'https://api.brainy.run/go/create_user', json = auth_body, auth=auth_brainy)
        self.id_user_auth = response_auth.json()['user_id"']
        