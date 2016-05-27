from django.conf.urls import url

from secode import views

urlpatterns = [
    url(r'^get/token$', views.GetCsrfToken(), name='get-token'),
    url(r'^create/list$', views.CreateList('POST'), name='create-list'),
    url(r'^delete/list$', views.DeleteList('POST'), name='delete-list'),
    url(r'^create/check$', views.CreateCheckToList('POST'), name='create-check'),
    url(r'^delete/check$', views.DeleteCheckFromList('POST'), name='delete-check'),
    url(r'^create/code$', views.CreateCodeAndCheck('POST'), name='add-code'),
]
