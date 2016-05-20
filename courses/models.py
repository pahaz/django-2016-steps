import markdown
from django.core.urlresolvers import reverse
from django.db import models

from core.models import Titled, Dated
from core.fields import JSONField


#  Course, Module


class Lesson(Titled, Dated):
    image = models.ImageField(upload_to='lesson_images', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('lesson', kwargs={'pk': self.pk})

    def __str__(self):
        return "lesson-{}".format(self.pk)


class Step(Dated):
    TYPE_MARKDOWN = 1
    TYPE_POLL = 2
    TYPE_CODE = 3
    TYPES = (
        (TYPE_MARKDOWN, 'markdown'),
        (TYPE_POLL, 'poll'),
        (TYPE_CODE, 'code'),
    )

    lesson = models.ForeignKey(Lesson, related_name='steps')
    type = models.IntegerField(choices=TYPES, editable=False)
    content = models.TextField(blank=True, null=True)
    meta = JSONField(blank=True, null=True)

    def render(self):
        if self.type == self.TYPE_MARKDOWN:
            return markdown.markdown(self.content)
        return '<step >'.format(repr(self.meta))

    def __str__(self):
        return "step-{}-{}".format(self.lesson_id, self.pk)
