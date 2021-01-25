from django.shortcuts import render, redirect, HttpResponse
from .models import ToDo, Book

def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, 'index.html', {'todo_list': todo_list})

def add_todo(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(homepage)

def edit(request):
    return render(request, 'edit.html')

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favourite = True
    todo.save()
    return redirect(homepage)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favourite = False
    todo.save()
    return redirect(homepage)

def books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', {'book_list': book_list})

def add_book(request):
    form = request.POST
    title = form['book_title']
    subtitle = form['book_subtitle']
    description = form['book_description']
    price = form['book_price']
    genre = form['book_genre']
    author = form['book_author']
    year = form['book_year']
    book = Book(title=title, subtitle=subtitle, description=description,\
    price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favourite = True
    book.save()
    return redirect(books)

def unmark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favourite = False
    book.save()
    return redirect(books)

