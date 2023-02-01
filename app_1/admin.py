from django.contrib import admin
from .models import Book, BookCard, LibraryVisitor, Author

admin.site.register(Book)
admin.site.register(BookCard)
admin.site.register(LibraryVisitor)
admin.site.register(Author)
