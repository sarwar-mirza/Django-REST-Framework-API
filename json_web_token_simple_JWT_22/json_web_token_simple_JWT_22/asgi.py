"""
ASGI config for json_web_token_simple_JWT_22 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'json_web_token_simple_JWT_22.settings')

application = get_asgi_application()
