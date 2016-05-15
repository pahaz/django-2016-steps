from django.db import models

from core.models import Titled, Dated


#  Course, Module


class Lesson(Titled, Dated):
    pass


class Step(Dated):
    lesson = models.ForeignKey(Lesson)
