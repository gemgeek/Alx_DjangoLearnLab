from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BookForm
from .forms import ExampleForm


def index(request):
    return HttpResponse("Hello from the bookshelf!")

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return render(request, 'bookshelf/book_create.html')  

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_edit.html', {'book': book})  

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    return HttpResponse("You have permission to delete this book.")  

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def search_book(request):
    books = []
    if request.method == "POST":
        user_input = request.POST.get('title', '')
        books = Book.objects.filter(title__icontains=user_input)

    return render(request, 'bookshelf/form_example.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})