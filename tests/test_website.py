def test_load_homepage(app, client):
    """Start page"""

    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Login Form Demo" in response.data
