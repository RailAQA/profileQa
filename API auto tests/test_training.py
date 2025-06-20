import requests
import pytest

def test_get_obj():
    url = "https://api.brainy.run/go/add_destination"
    body = {
  "name": "New York"
}
    auth = ('login', 'pass')
    response = requests.post(url, json = body, auth = auth).json()
    assert requests.post(url, json = body, auth = auth).status_code == 201