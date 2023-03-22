from django.contrib import admin
from  .models import Author, Book, Genre, Language, Status, BookInstance

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ("Экземпляры книг", {'fields': ("book", "imprint", "inv_nom")}),
        ("Статус и окончание его действия", {'fields': ("status", "due_back")})
    )

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)



