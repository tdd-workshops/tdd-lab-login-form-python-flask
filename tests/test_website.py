import requests
import pytest

url = "http://localhost:5000/"


@pytest.mark.smoke
def test_home_page():
    response = requests.get(url)

    response.status_code == 200
