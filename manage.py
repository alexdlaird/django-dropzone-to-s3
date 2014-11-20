#!/usr/bin/env python
import os
import sys

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangodropzonetos3.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
