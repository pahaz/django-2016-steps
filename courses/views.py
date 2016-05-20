from courses.models import Lesson
from django.views.generic import ListView, DetailView


class LessonListView(ListView):
    queryset = Lesson.objects.all()
    template_name = 'courses/lesson_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    template_name = 'courses/lesson.html'
    queryset = Lesson.objects.all()
    context_object_name = 'lesson'
