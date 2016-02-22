# Farm-hands
koding.com hackathon app

## Getting Started


## Installation
1. Clone the repository and create a Virtual Environment. 
- Run `virtualenv <virtualenvname>` or `mkvirtualenv <virtualenvname>` if using virtualenv wrapper to create the virtual environment.
2. Install all the necessary requirements by running `pip install -r requirements.txt` within the virtual environment.
3. Configure your database configurations in a development.py and save in the settings folder. Also git ignore your development.py file



### development.py

```

from .base import *


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

```

### Run server
To run your server
```
gunicorn farmhands.wsgi --pythonpath=farmhands --log-file=-
```
