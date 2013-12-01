from django.test import TestCase

import os
import sys
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('sb_proj'))
import sb_proj
os.environ['DJANGO_SETTINGS_MODULE'] = 'sb_proj.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sb_proj.settings")