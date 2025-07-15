from endpoints.create_corporation_enp import CreateCorporationEnp
import pytest
from endpoints.create_user_enp import CreateUserEndp

# Тест-кейс 1
def test_add_corp_with_1name():
    auth_enp = CreateUserEndp()
    auth_enp.create_user()
    auth = ('a', "a")
    body = {
  "description": "Не ешь свои фрукты",
  "logo_url": "https://brainy.run/wp-content/uploads/2025/01/robbie.jpg",
  "name": "А",
  "owner_id": 321
}
    endpoint = CreateCorporationEnp()
    endpoint.create_corporation(auth, body)

