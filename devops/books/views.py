from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from books.models import books


# Create your views here.


def home(request):
    # booksinfo = [
    #     {"id": 1, "name": "book1", "description": "book1_description"},
    #     {"id": 2, "name": "book2", "description": "book2_description"},
    #     {"id": 3, "name": "book3", "description": "book3_description"}
    # ]
    booksinfo = books.objects.all()
    return render(request, "books/home.html", context={"data": booksinfo})


def contactus(request):
    return render(request, "books/contactus.html")


def aboutus(request):
    return render(request, "books/aboutus.html")


def get_book_datails(request, id):
    book = get_object_or_404(books, id=id)
    return render(request, "books/showbook.html", context={"book": book})


def delete_book(request, id):
    book = get_object_or_404(books, id=id)
    book.delete()
    return redirect("home")
