[![Coverage Status](https://coveralls.io/repos/github/LimaGuilherme/flask-boilerplate/badge.svg?branch=master)](https://coveralls.io/github/LimaGuilherme/flask-boilerplate?branch=master)

[![Maintainability](https://api.codeclimate.com/v1/badges/d0489978ee823f5e53eb/maintainability)](https://codeclimate.com/github/LimaGuilherme/flask-boilerplate/maintainability)

![Python application](https://github.com/LimaGuilherme/flask-boilerplate/workflows/Python%20application/badge.svg)

 # Requirements
    Linux
    Python 3+
    Pip3
    Virtualenvwrapper (Optional but highly recommended)
    PostgreSQL 10+
  
    
 # Installing
 
     $ git clone git@github.com:LimaGuilherme/flask-boilerplate.git
     $ mkvirtualenv -p python3 flask-boilerplate
     $ workon flask-boilerplate
     $ pip install -r requirements.txt
     $ pip install -r requirements_dev.txt
 
 Dealing with environments variables

    $ cd
    $ vim .bashrc
    
    Add this in the end of file and reopen the terminal
    alias load-env='export $(cat .env | xargs)'
    alias load-env-test='export $(cat .env.test | xargs)'
    
    $ load-env
    
 Setting up database

    $ sudo apt-get install postgres
    
    $ sudo su postgres
    $ psql
    $ CREATE ROLE flask SUPERUSER LOGIN PASSWORD 'flask';
    $ CREATE DATABASE flask;
    $ CREATE DATABASE flask_test;
    $ ALTER DATABASE flask OWNER TO flask;
    $ ALTER DATABASE flask_test OWNER TO flask;
    $ \q
    $ exit

Create a .env file based on .env.sample, with your custom configuration (if necessary) and then:

    $ load-env
    $ python manage.py db upgrade
    
    
 # Built With
* Alembic - lightweight database migration tool for usage with the SQLAlchemy Database Toolkit
* Boto3 - AWS SDK for Python, which allows Python developers to write software that makes use of services like S3.
* Celery - Distributed task queue
* Coveralls - Python interface to coveralls.io API
* coverage - Code coverage measurement for Python
* Flask - The web framework used


# Authors
Guilherme Lima - Initial work

# License
This project is licensed under the MIT License - see the LICENSE.md file for details