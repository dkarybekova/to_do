"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import homepage, add_todo, edit, delete_todo, mark_todo, unmark_todo, close_todo, \
books, add_book, delete_book, mark_book, unmark_book, book_detail

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('https://todoexample.com/', homepage, name='home'),
    path('add/', add_todo, name='add_todo'),
    path('edit/', edit, name='edit'),
    path('delete/<id>/', delete_todo, name='delete-todo'),
    path('mark/<id>/', mark_todo, name='mark-todo'),
    path('unmark/<id>/', unmark_todo, name='unmark-todo'),
    path('close/<id>/', close_todo, name='close-todo'),
    path('books/', books, name='books'),
    path('add-book/', add_book, name='add_book'),
    path('book-detail/<id>/', book_detail, name='book-detail'),
    path('delete-book/<id>/', delete_book, name='delete-book'),
    path('mark-book/<id>/', mark_book, name='mark-book'),
    path('unmark-book/<id>/', unmark_book, name='unmark-book'),
]   +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

