from django.contrib import admin
from .models import Book

# Custom admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to display
    list_filter = ('publication_year', 'author')  # filters in sidebar
    search_fields = ('title', 'author')  # search bar

# Register model with custom admin settings
admin.site.register(Book, BookAdmin)