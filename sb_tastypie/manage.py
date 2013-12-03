#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":

    sys.path.append(os.path.abspath('..'))
    sys.path.append(os.path.abspath('sb_proj'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sb_proj.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
