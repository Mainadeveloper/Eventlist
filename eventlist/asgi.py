"""
ASGI config for eventlist project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventlist.settings')

application = get_asgi_application()
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
