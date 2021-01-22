"""
WSGI config for Shopify project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os,sys

sys.path.append("C:/Users/Administrator/Desktop/Shopify/venv/Lib/site-packages")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shopify.settings')

application = get_wsgi_application()
