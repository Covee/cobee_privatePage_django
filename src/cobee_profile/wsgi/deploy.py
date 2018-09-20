import os, sys

path = os.path.abspath(__file__+'/../..')

if path not in sys.path:
	sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cobee_profile.settings.deploy")

application = get_wsgi_application()