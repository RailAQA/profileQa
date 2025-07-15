import requests
from faker import Faker

def autorization_role_owner():
    auth = ('rgn23', "Railka123")
    fake = Faker("en_EN")
    fake_ru = Faker('ru_Ru')
    payload_autorization = {
  "avatar_url": "https://brainy.run/wp-content/uploads/2024/05/candidate2.png",
  "email": fake.hostname(),
  "name": fake_url.last_name_male(),
  "password": "superpassword",
  "role": "owner",
  "username": fake.last_name()
}
    authorization = requests.post(auth=auth, json=payload_autorization)
    authorization.json