# City Weather

## Overview

A service that authenticates users and displays the temprature of the requeested city

---

## Configuration and Installation

1. Create an account in **https://openweathermap.org/**. An email will be sent with your **API KEY**.
2. Inside a shell (it will be available only for the current shell session) or inside **~/.bashrc** (for all shell sessions), store the variable **API KEY** that you have received in your email -> `export API_KEY='<RECEIVED_API_KEY>'`
3. Clone the project -> `git clone https://github.com/MShbana/city-weather.git city_weather`
4. Change directory into the cloned project -> `cd city_weather`
5. Create a virtual environment in the project's parent directory -> `python3 -m venv ../env`
6. Activate the vritual environment `source ../env/bin/activate`
7. Install the required software -> `pip install -r requirements.txt`
8. Generate the SQL commands for the database changes -> `python manage.py makemigrations`
9. Execute those SQL commands -> `python manage.py migrate`
10. Run the server on port 8000 -> `python manage.py runserver`
11. Access the web application on **http://localhost:8000**

---

## How to Use

### APIS

#### Return all registered users (Available for Admins only)

- GET request to `/api/users/`.
- Sample Response:

``` 
    [
        {
            "username": "<username>",
            "email": "<email>",
            "first_name": "<first_name>",
            "last_name": "<last_name>"
        },
        {
            "username": "<username>",
            "email": "<email>",
            "first_name": "<first_name>",
            "last_name": "<last_name>"
        },
        {
            "username": "<username>",
            "email": "<email>",
            "first_name": "<first_name>",
            "last_name": "<last_name>"
        },
        .
        .
        .
    ]
```

#### Register a new user

- POST request to `/api/users/`.
- Sample POST:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>",
        "password": "<password>"
    }
```

- Sample Resposne:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>"
    }
```

#### Return the details of a specific user by ID (Available for Admins only)

- GET request to `/api/users/<pk>`.
- Sample Response:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>"
    }
```

#### Delete a specific user by ID (Available for Admins only)

- DELETE request to `/api/users/<pk>`.
- Sample DELETE:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>"
    }
```

#### Update the details of a specific user by ID (Available for Admins only)

- PUT request to `/api/users/`.
- Sample PUT:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>"
    }
```

#### Return the details of the current logged-in user

- GET request to `/api/auth/user/`.
- Sample Response:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>"
    }
```

#### Update the details of the current logged-in user

- PUT request to `/api/auth/user/`
- Sample PUT:

``` 
    {
        "username": "<username>",
        "email": "<email>",
        "first_name": "<first_name>",
        "last_name": "<last_name>"
    }
```

#### Return the REST Token if the credentials are valid and authenticated (User Login)

- POST request to `/api/auth/login/`
- Sample POST (email not required):

``` 
    {
        "username": "<username>",
        "email": "<email>"
        "password": "<passowrd>"
    }
```

- Sample Response:

``` 
    {
        "token":"eyJ0eXAiOiJKV1QiLCJhbGciO....",
        "user":
        {
            "pk": <id>,
            "username": "<username>",
            "email": "<email>",
            "first_name": "<first_name>",
            "last_name": "<last_name>"
        }
    }
```

#### Delete the Token object assigned to the User (User Logout)

- POST request to `/api/auth/logout/`
- Sample Response:

``` 
    {
        "detail": "Successfully logged out."
    }
```

#### Change Password for the current logged in user

- POST request to `/api/auth/password/change/`
- Sample POST:

``` 
    {
        "new_password1": "<password>",
        "new_password2": "<password_confirm>"
    }
```

- Sample Response

``` 
    {
        "detail": "New password has been saved."
    }
```
