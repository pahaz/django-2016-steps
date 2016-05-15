from django.db import models


class Titled(models.Model):
    title = models.CharField(max_length=512)

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
