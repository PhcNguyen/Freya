from django.conf import settings
settings.configure('freya/settings.py')

from django.utils import timezone
import datetime
print(timezone.now())

print(timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone()))
