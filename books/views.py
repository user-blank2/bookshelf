from django.shortcuts import render
from .models import Books

# Create your views here.

# get all books from the database
def book_list(request):
  books = Books.objects.all()
  return render(request,'books/book_list.html',{'books':books})