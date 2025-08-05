from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (GET) or create a new one (POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to view, but only logged-in users to create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Same permission setup
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
