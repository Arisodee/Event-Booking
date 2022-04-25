# Event Booking

#### Author: [Ariso Okanga](https://github.com/Arisodee)

## Description
This web application allows users to post upcoming events, see events posted by others and book these events.

A user will be able to:

1. Sign up and log in
2. Post their event and have other users book them
3. View events posted by other users and book them
4. Update and delete their events


## Technologies Used
- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgresql
- Heroku

### Prerequisite
This project requires a prerequisite understanding of the following:
- Django Framework
- Python3.6
- Postgres
- Python virtual env

## Setup and installation

#### Clone the Repository
####  Activate virtual environment
Create and activate virtual environment using python3.6 as default handler
    `python3.6 -m venv virtual && source virtual/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE myevents;
####  .env file
Create a file named`.env`  and copy paste the following filling-in where appropriate:
```
SECRET_KEY='<your secret key>'
DEBUG=True
DB_NAME='myevents'
DB_USER='<your database username>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```
#### Run initial Migration
python3.6 manage.py makemigrations events
python3.6 manage.py migrate

#### Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000


## Support and contact details
Incase you come across errors, have any questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at : arisodee@gmail.com

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
