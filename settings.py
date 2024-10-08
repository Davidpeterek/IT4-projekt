DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',  # Jmeno služby z docker-compose.yml
        'PORT': '5432',
    }
}
