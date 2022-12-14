from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    booksinfo = [
        {"id": 1, "name": "book1", "description": "book1_description"},
        {"id": 2, "name": "book2", "description": "book2_description"},
        {"id": 3, "name": "book3", "description": "book3_description"}
    ]
    return render(request, "books/home.html", context={"data": booksinfo})


def contactus(request):
    return render(request, "books/contactus.html")


def aboutus(request):
    return render(request, "books/aboutus.html")
