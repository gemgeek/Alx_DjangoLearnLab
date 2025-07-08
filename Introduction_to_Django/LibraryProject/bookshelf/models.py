# LibraryProject/bookshelf/models.py 📚

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        # This method defines the string representation of a Book object.
        # It's very useful for displaying objects in the Django admin
        # and in the shell in a human-readable way.
        return f"{self.title} by {self.author} ({self.publication_year})"