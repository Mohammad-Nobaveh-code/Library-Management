from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('author.urls')),
    path('', include('book.urls')),
    path('', include('debt.urls')),
    path('', include('extra.urls')),
    path('', include('loan.urls')),
]
