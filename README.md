<h1 align="center">Stock Market API Service 💸</h1>


### ✨ [Admin Panel](http://example.com/admin)
### ✨ [Swagger API Documentation](http://example.com/api/docs)

<br/>

## Prerequisites

⚡ **Generate file .env using .env.sample as guide and then fill out with a real API_KEY for Alpha Vantage**

* Docker Desktop
* Docker Compose


## Install

```sh
# in terminal
docker build .
docker-compose up

# in another terminal
docker-compose run --rm app  sh -c "python manage.py createsuperuser"

```

## Usage

```sh
# in terminal
docker-compose up

# In browser
http://localhost:8000/api/docs   (API Docs)



# In api/docs
/api/user/create/ (User Sign up)
/api/user/token/  (Creates Authorization Token)

# Protected dndpoints via tokenAuth
/api/stocks/{id}/  (Stock information)
/api/stocks/       (Request logs for authenticated user)
/api/user/me/      (User Profile)
```

## Run tests

```sh
docker-compose run --rm app  sh -c "python manage.py test"
```

## Run linter

```sh
docker-compose run --rm app  sh -c "flake8"
```

## Developers

👤 **Zayter Munive**

* Github: [@zayter](https://github.com/zayter)
