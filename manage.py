#!/usr/bin/env python
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = REPO_ROOT / 'proyecto'

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

from django.core.management import execute_from_command_line


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
