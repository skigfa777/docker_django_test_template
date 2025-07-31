"""
ASGI config for test2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
from pathlib import Path
import environ, os

env = environ.Env()
environ.Env.read_env(env_file=Path('../.env'))

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', (env('DJANGO_PROJECT_NAME') + '.settings'))

application = get_asgi_application()
