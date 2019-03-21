from HeartMap.settings.base import *

# Override base.py settings here

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from HeartMap.settings.local import *
except:
pass