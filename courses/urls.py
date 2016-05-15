from courses.views import run_code
from django.conf.urls import url
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        name = str(request.user)
    return render(request, 'index.html', {'name': request.user})


urlpatterns = [
    url(r'^$', run_code),
]
