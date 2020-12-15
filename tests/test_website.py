from unittest.mock import patch


def test_load_homepage(app, client):
    """Start page"""

    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Login Form Demo" in response.data


def test_signup_page(app, client):
    """Signup page"""

    response = client.get('/signup')
    assert response.status_code == 200
    assert b"Signup for an account" in response.data


def test_create_user_account(app, client):
    """Create user account"""

    with patch('db.insert_employee') as insert_employee_mock:
        response = client.post('/signup', data=dict(
            username='demo1',
            password='xxx',
            password_confirm='xxx',
            email='demo1@example.com'
        ), follow_redirects=True)

        assert response.status_code == 200
        assert b"Welcome back" in response.data
        insert_employee_mock.assert_called_with('demo1', 'demo1@example.com', 'xxx')


def test_create_with_mismatched_password(app, client):
    """Invalid signup details"""

    with patch('db.insert_employee') as insert_employee_mock:
        response = client.post('/signup', data=dict(
            username='demo1',
            password='xxx',
            password_confirm='xxx1',
            email='demo1@example.com'
        ), follow_redirects=True)

        assert response.status_code == 200
        assert b"Invalid user registration" in response.data
        insert_employee_mock.assert_not_called()


def dummy_get_all_employees():
    yield 'a_username', 'demo@example.com', 'demo1234'


def test_valid_login(app, client):
    """Valid login details"""

    with patch('db.get_all_employees', dummy_get_all_employees):
        response = client.post('/signin', data=dict(
            email='demo@example.com',
            password='demo1234',
        ), follow_redirects=True)

        print(response.data)
        assert response.status_code == 200
        assert b"Welcome back" in response.data


def test_invalid_login(app, client):
    """Invalid login details"""

    with patch('db.get_all_employees', dummy_get_all_employees):
        response = client.post('/signin', data=dict(
            email='wrong@example.com',
            password='xxx',
        ), follow_redirects=True)

        assert response.status_code == 200
        assert b"Invalid username/password" in response.data
