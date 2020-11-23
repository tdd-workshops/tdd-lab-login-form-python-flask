# Login Form Demo

This repository contains a simple web application written in Python.

## Workshop

The product owner is very happy with the application, but would like some enhancements.

### User Story

> As a **User**, <br>
**When** I login with password which is too short.<br>
**Then** I should see an alert telling me my password is too short.

Acceptance Criteria:

- Error alert should be visible when the password is too short.
- This should be a server-side implementation.
- There should be additional automated test coverage.

---

## Running the application

Open this folder in your terminal app. And run these commands in the terminal.

1. Create virtual environment 

    ```
    pipenv shell
    ```

2. Installing packages

    ```
    pipenv install -r requirements.txt
    ```
    
    You can open this url in your browser to view the app: <http://localhost:3000>
    
3. To run the test:
    
    Here are the options for `pytest`
    * `v` - The verbose view of test case
    ```
    pytest -v
    ```
    
    * `m` - The label that is given for [custom marker](https://docs.pytest.org/en/stable/example/markers.html) to 
    run the specific tests. 

    ```
    pytest -m smoke
    ```

    * `vm` - Displays specific test cases under custom marker in verbose mode. The default smoke requires your flask app
     to be running for it to work. 

    ```
    pytest -vm smoke
    ```
   
4. To run the web application
   ```
   flask run
   ```   

## Python Packages

- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)** - Python web framework used for the web application.
- **[Jinja](https://flask.palletsprojects.com/en/1.1.x/templating/)** - Templating engine for displaying the HTML pages.
- **[Pytest](https://docs.pytest.org/en/stable/)** - Python testing framework
- **[Requests](https://requests.readthedocs.io/en/master/)** - Elegant and simple HTTP library for Python
- **[Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)** - Python Dev Workflow for Humans

## Routes

1. `GET /`

    This is the home page. The login form is also here.

2. `GET /users`
    This is how you login to the app. You will need to login with `email` and `password`.

    The default email is `demo@example.com` and password is `demo1234`.

2. `POST /users` 
    The backend API for user authentication of user credentials 

    The default email is `demo@example.com` and password is `demo1234`.

3. `GET /users/welcome`

    Landing page after you have successfully logged in with the correct credentials.

4. `GET /users/logout`

    URL for logging out of the application.