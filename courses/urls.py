from courses.views import LessonListView, LessonDetailView
from django.conf.urls import url


urlpatterns = [
    url(r'^lessons/$', LessonListView.as_view(), name='lesson_list'),
    url(r'^lessons/(?P<pk>[\w-]+)/$', LessonDetailView.as_view(),
        name='lesson'),
]
