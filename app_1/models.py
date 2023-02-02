from django.db import models


# HOME LIBRARY
class BookShelfAuthor(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class BookShelf(models.Model):
    book_title = models.CharField(max_length=255)
    book_code = models.CharField(max_length=255)
    author = models.ForeignKey(BookShelfAuthor, on_delete=models.PROTECT)


# PUBLIC LIBRARY
class Author(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class LibraryVisitor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BookCard(models.Model):
    visitor = models.ForeignKey(LibraryVisitor, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.book} taken by {self.visitor}'
