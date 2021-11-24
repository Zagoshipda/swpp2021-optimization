import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "item.settings")

import django
django.setup()


from app.models import Item
from time import time

start = time()
count = len(Item.objects.all())
print('Not optimal: {:3f} ms'.format((time() - start) * 1000))

start = time()
count = Item.objects.count()
print('Optimal: {:3f} ms'.format((time() - start) * 1000))