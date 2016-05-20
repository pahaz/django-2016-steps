import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_project_.settings")
django.setup()

# -----------------------------------

from django.contrib.auth.models import User

User.objects.create_superuser('qwer', 'qwe@qwe.qq', 'qwer')
