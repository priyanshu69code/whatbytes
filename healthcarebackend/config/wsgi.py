# wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(settings.BASE_DIR, 'staticfiles'))
