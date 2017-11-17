#!/usr/bin/env python
import os
import sys

# python manage.py runserver 0.0.0.0:8000
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amsStudy.settings")

    from django.core.management import execute_from_command_line

    # sys.argv = manage.py runserver 0.0.0.0:8000
    execute_from_command_line(sys.argv)
