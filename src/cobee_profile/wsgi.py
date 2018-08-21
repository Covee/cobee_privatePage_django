"""
WSGI config for cobee_profile project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# settings파일을 분리하고 나면 이 파일의 project_name.settings 뒤에 새로운 경로를 추가로 작성 해 주어야 함.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cobee_profile.settings.base')

application = get_wsgi_application()
