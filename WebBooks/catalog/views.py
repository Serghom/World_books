from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from  .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.object.all().count()
    num_instances = BookInstance.object.all().count()

    num_instances_available = BookInstance.object.filter(status__exact=2).count()

    num_authors = Author.object.count()

    return render(request, "index.html", context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4