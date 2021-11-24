import random
import string

from django.http import HttpResponse, HttpResponseNotAllowed

from .models import Item

def create_item(request):
    if request.method == 'GET':
        charset = string.ascii_letters + string.digits
        random_name = ''.join(random.choices(charset, k=20))

        Item.objects.create(name=random_name)

        return HttpResponse('OK')
    else:
        return HttpResponseNotAllowed(['GET'])