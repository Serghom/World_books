from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from  .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.object.all().count()
    num_instances = BookInstance.object.all().count()

    num_instances_available = BookInstance.object.filter(status__exact=2).count()

    num_authors = Author.object.count()

    # Количество посещений этого view, подсчитаное переменой session
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    return render(request, "index.html", context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors,
                                                  'num_visits': num_visits})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    '''
    Универальный класс предтавления списка книг, находящихся в заказе у текущего пользователя
    '''

    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.object.filter(borrower=self.request.user).filter(status__exact="2").order_by("due_back")