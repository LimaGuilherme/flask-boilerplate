
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
flask-CORS - A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
Flask Migrate - an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
Flask-RESTful - an extension for Flask that adds support for quickly building REST APIs
gunicorn - a Python WSGI HTTP Server for UNIX
mock - mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
passlib - comprehensive password hashing framework
pip - Dependency Management
Psycopg - PostgreSQL adapter for the Python programming language
SQLAlchemy - Python SQL toolkit and Object Relational Mapper
SQLAlchemy-Utils - Various utility functions for SQLAlchemy.
testtools - testtools is a set of extensions to Python’s standard unittest module.

# Authors
Guilherme Lima - Initial work

# License
This project is licensed under the MIT License - see the LICENSE.md file for details