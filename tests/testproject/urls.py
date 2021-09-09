import time

from django.urls import path
from django.shortcuts import render
from django.utils.timezone import now


def test_view(request):
    return render(request, 'test.txt', {
        'date': now(),
        'number': time.time(),
        'locale': request.locale,
    })


urlpatterns = [
    path('', test_view),
]
