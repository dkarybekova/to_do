from django.shortcuts import render, HttpResponse
from .models import ToDo, Book

def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, 'index.html', {'todo_list': todo_list})

def add(request):
    return render(request, 'add.html')

def edit(request):
    return render(request, 'edit.html')

def delete(request):
    return render(request, 'delete.html')

def books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', {'book_list': book_list})

