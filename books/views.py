from django.shortcuts import get_object_or_404, redirect, render
from .models import Books
from .forms import BookForm

# Create your views here.

# get all books from the database
def book_list(request):
  input = request.GET.get('q','')
  if input:
    books = Books.objects.filter(title__icontains=input) | Books.objects.filter(author__icontains=input)
  else:
    books = Books.objects.all()
    
  return render(request,'books/book_list.html',{'books':books,'query':input})


def add_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = BookForm()
    
  return render(request,'books/add_book.html',{'form':form})  

def edit_book(request,pk):
  book = get_object_or_404(Books,pk=pk)
  if request.method == 'POST':
    form = BookForm(request.POST,instance=book)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = BookForm(instance=book)

  return render(request,'books/edit_book.html',{'form':form,'book':book})

def delete_book(request,pk):
  book = get_object_or_404(Books,pk=pk)
  if request.method == 'POST':
    book.delete()
    return redirect('book_list')
  return render(request,'books/delete_book.html',{'book':book})

