"""
WSGI config for StageSolixyPy Collection.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoCollection.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StageSolixyPy.settings')

application = get_wsgi_application()
