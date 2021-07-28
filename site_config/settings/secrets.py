import os
import json
from django.core.exceptions import ImproperlyConfigured

with open('secrets.json') as file:
    secrets = json.loads(file.read())

def get_secrets(var_name, limits:str, secret=secrets):
    if limits == 'secret':
        try:
            return secret[var_name]
        except KeyError:
            error_msg = f'No secret named {var_name}'
            raise ImproperlyConfigured(error_msg)

    elif limits == 'envs':
        try:
            return os.environ[var_name]
        except KeyError:
            error_msg = f'No variable named {var_name}'
            raise ImproperlyConfigured(error_msg)