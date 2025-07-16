from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
