from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name