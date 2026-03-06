from django.shortcuts import redirect, render
from .models import Books
from .forms import BookForm

# Create your views here.

# get all books from the database
def book_list(request):
  books = Books.objects.all()
  return render(request,'books/book_list.html',{'books':books})


def add_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = BookForm()
    
  return render(request,'books/add_book.html',{'form':form})  