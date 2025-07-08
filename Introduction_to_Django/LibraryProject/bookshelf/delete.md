# Delete Operation

```python
from bookshelf.models import Book

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")  # Get the book by its updated title

book_to_delete.delete()  # Delete it
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# <QuerySet []>