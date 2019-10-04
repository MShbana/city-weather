# City Weather

## Overview

A service that authenticates users and displays the temprature of the requeested city

## Installation

1. `git clone https://github.com/MShbana/city-weather.git city_weather`
2. `cd city_weather`
3. `python3 -m venv ../env`
4. `source ../env/bin/activate`
5. `pip install -r requirements.txt`
6. `python manage.py makemigrations`
7. `python manage.py migrate`
8. `python manage.py runserver`

--

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
