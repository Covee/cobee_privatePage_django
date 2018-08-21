#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # settings파일을 분리하고 나면 이 파일의 project_name.settings 뒤에 새로운 경로를 추가로 작성 해 주어야 함.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cobee_profile.settings.base')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
