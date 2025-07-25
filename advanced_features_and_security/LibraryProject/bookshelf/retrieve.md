# Retrieve Operation

```python
retrieved_book = Book.objects.get(title="1984")

print(retrieved_book.title)
# 1984

print(retrieved_book.author)
# George Orwell

print(retrieved_book.publication_year)
# 1949