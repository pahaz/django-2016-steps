from courses.models import Lesson, Step

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.crypto import get_random_string


class TestListView(TestCase):
    def make_lesson(self):
        return Lesson.objects.create(title=get_random_string())

    def make_step(self, type=Step.TYPE_MARKDOWN, meta=None, lesson=None,
                  content=None):
        if not meta:
            meta = get_random_string()
        if not lesson:
            lesson = self.make_lesson()
        if not content:
            content = get_random_string()
        return Step.objects.create(type=type, meta=meta, lesson=lesson,
                                   content=content)

    def test_lesson_list_url(self):
        url = reverse('lesson_list')
        self.assertEqual(url, '/lessons/')

    def test_lesson_url(self):
        lesson = self.make_lesson()
        url = reverse('lesson', kwargs={'pk': lesson.pk})
        self.assertEqual(url, '/lessons/' + str(lesson.pk) + '/')

    def test_lesson_list_contain_titles(self):
        lesson = self.make_lesson()
        response = self.client.get(reverse('lesson_list'))
        self.assertContains(response, lesson.title)
        self.assertContains(response, lesson.get_absolute_url())

    def test_lesson_contain_step_md_content(self):
        lesson = self.make_lesson()
        step = self.make_step(lesson=lesson, type=Step.TYPE_MARKDOWN)
        response = self.client.get(lesson.get_absolute_url())
        self.assertContains(response, lesson.title)
        self.assertContains(response, step.content)
