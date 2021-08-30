import os 
BASE_DIR = os.Path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.Path.join(BASE_DIR, 'db.sqlite3'),
    }
}