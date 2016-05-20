from django.db import models


class Titled(models.Model):
    title = models.CharField(max_length=512)

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True
