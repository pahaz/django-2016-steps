from django.conf.urls import url

from secode import views

urlpatterns = [
    url(r'^get-token$', views.get_csrf_token, name='get-token'),
    url(r'^create-list$', views.create_list, name='create-list'),
    url(r'^delete-list$', views.delete_list, name='delete-list'),
    url(r'^create-check$', views.add_check_to_list, name='create-check'),
    url(r'^delete-check$', views.delete_check_from_list, name='delete-check'),
    url(r'^add-code$', views.add_and_check_code, name='add-code'),
]
