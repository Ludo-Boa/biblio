from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Author)
# Définir la classe admins
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Enregistrez la classe admin avec le modèle associé
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
admin.site.register(Language)

# admin.site.register(Book)
# admin.site.register(BookInstance)
# Enregistrez les classes Admin pour Book à l'aide du décorateur
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Enregistrez les classes Admin pour BookInstance à l'aide du décorateur
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Disponibilité', {
            'fields': ('status', 'due_back')
        }),
    )


