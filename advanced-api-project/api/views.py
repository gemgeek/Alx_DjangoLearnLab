from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


"""
BookListView:
- Supports filtering by title, author name, and publication_year.
- Allows search across title and author name using the 'search' query param.
- Supports ordering by title and publication_year using 'ordering' param.

Examples:
- /books/?search=Python
- /books/?author__name=John&publication_year=2023
- /books/?ordering=-publication_year
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering/searching/ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define the fields to filter by
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Define which fields can be searched
    search_fields = ['title', 'author__name']

    # Define default ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
This module contains generic API views for the Book model.

- BookListCreateView:
    Handles listing all books and creating new ones.
    Only authenticated users can create.

- BookDetailView:
    Handles retrieving, updating, and deleting a specific book.
    Only authenticated users can modify or delete.
"""