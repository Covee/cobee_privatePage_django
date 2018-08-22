import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cobee_profile.settings.debug")

application = get_wsgi_application()