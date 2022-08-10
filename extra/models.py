from django.db import models


class Like(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    vote = models.BooleanField()
    create = models.DateTimeField(auto_now_add=True)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
