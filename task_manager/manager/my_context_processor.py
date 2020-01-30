from datetime import time

import django


def my_cp(request):
    context = {
        'now' : django.utils.timezone.now(),
        'version': '1.0',
    }
    return context
