# Delete Operation

```python
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")  # Get the book by updated title

book_to_delete.delete()  # Delete it

# (1, {'bookshelf.Book': 1})

Book.objects.all()
# <QuerySet []>