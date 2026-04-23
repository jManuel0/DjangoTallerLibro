import os
import sys
from pathlib import Path

import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

if os.getenv('VERCEL') and not os.getenv('DATABASE_URL'):
    django.setup()
    call_command('migrate', interactive=False, run_syncdb=True, verbosity=0)

application = get_wsgi_application()
app = application
