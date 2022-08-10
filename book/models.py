from django.db import models


class Book(models.Model):
    class MyManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(active=True)

    name = models.CharField(max_length=50)
    cover = models.ImageField(default='default.jpg', upload_to='bookcover/')
    create = models.DateTimeField(auto_now_add=True)
    modifield = models.DateTimeField(auto_now=True)
    desc = models.TextField(max_length=1000)
    translator = models.CharField(max_length=200)
    publisher = models.ForeignKey('extra.Publisher', on_delete=models.CASCADE)
    category = models.ManyToManyField('extra.Category')
    author = models.ManyToManyField('author.Author')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    active = models.BooleanField()
    loan = models.ForeignKey('loan.Loan', on_delete=models.PROTECT, related_name='loan_book', null=True)

    objects = models.Manager()
    pubs = MyManager()

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title