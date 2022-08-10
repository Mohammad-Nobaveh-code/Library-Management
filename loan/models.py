from django.db import models

from book.models import Book


class Loan(models.Model):
    statuses = (
        ('C', 'choosing'),
        ('S', 'started'),
        ('R', 'returned'),
        ('T', 'to_be_returned'),
    )

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=statuses)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loan_book', null=True)


class Debt(models.Model):
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.amount}'
