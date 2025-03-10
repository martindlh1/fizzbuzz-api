import pytest
from src.controller import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_fizzbuzz(client):
    # Test case 1
    response = client.post('/fizzbuzz', json={'fizz_nb': 2, 'buzz_nb': 5, 'start': 1, 'end': 10})
    assert response.status_code == 200
    assert response.json == ['1', 'fizz', '3', 'fizz', 'buzz', 'fizz', '7', 'fizz', '9', 'fizzbuzz']

    # Test case 2
    response = client.post('/fizzbuzz', json={'fizz_nb': 3, 'buzz_nb': 5, 'start': 1, 'end': 15})
    assert response.status_code == 200
    assert response.json == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14',
                             'fizzbuzz']
