# Update Operation

```python
book_to_update = Book.objects.get(title="1984")  # Get the book by its current title

book_to_update.title = "Nineteen Eighty-Four"  # Change the title

book_to_update.save()  # Save the changes to the database

updated_book = Book.objects.get(author="George Orwell")  # Retrieve again to confirm the update

print(updated_book.title)
# Nineteen Eighty-Four