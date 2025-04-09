from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form': form })
    
def logout_view(request):
        logout(request)
        return redirect('login')
    
@login_required
def book_list(request):
    Books = Book.objects.all()
    return render(request, 'book_list.html',{'books': Books})
    
@login_required
def book_detail(request, slug):
    Book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_detail.html',{'book': Book})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book = form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

    























































# def create_task(request):
#     form = BookForm()

#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     return render(request, 'book_form.html', {'form':form})

# def book_list(request):
#     book = Book.objects.all()
#     return render(request, 'book_list.html', {'book': book})

# def book_detail(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     return render(request, 'task_detail.html', {'book': book})

# def book_update(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     form = BookForm(instance=book)

#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
        
#     return render(request, 'book_form.html', {'form':form})

# def book_delete(request, slug):
#     task = get_object_or_404(Book, slug=slug)
#     task.delete()
#     return redirect('book_list')
    
