from django.contrib import admin
from .models import Book, Bookmark, Comment

admin.site.register(Book)
admin.site.register(Bookmark)
admin.site.register(Comment)
