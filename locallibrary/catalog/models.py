from django.db import models

# Create your models here.

class Genre(models.Model):
    """Cet objet représente une catégorie ou un genre littéraire."""
    name = models.CharField("Genre", max_length=200, help_text='Entrez un genre de livre  (ex. Science Fiction)')

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name


from django.urls import reverse # Cette fonction est utilisée pour formater les URL

class Book(models.Model):
    """Cet objet représente un livre (mais ne traite pas les copies présentes en rayon)."""
    title = models.CharField(verbose_name="Titre", max_length=200)

    # La clé étrangère (ForeignKey) est utilisée car elle représente correcte le modèle de relation en livre et son auteur :
    #  Un livre a un seul auteur, mais un auteur a écrit plusieurs livres.
    # Le type de l'objet Author est déclré comme une chaîne de caractère car
    # la classe d'objet Author n'a pas encore été déclarée dans le fichier
    author = models.ForeignKey('Author', verbose_name="Auteur", on_delete=models.SET_NULL, null=True)

    summary = models.TextField(verbose_name="Résumé", max_length=1000, help_text='Entrez une brève description du livre')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 caractères <a href="https://www.isbn-international.org/content/what-isbn">numéro ISBN</a>')

    # Le type ManyToManyField décrit correctement le modèle de relation en un livre et un genre.
    #  un livre peut avoir plusieurs genres littéraire et réciproquement.
    # Comme la classe d'objets Genre a été définit précédemment, nous pouvons manipuler l'objet.
    genre = models.ManyToManyField(Genre, help_text='Sélectionnez un genre pour ce livre')

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets Book dans la base de données."""
        return self.title

    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('book-detail', args=[str(self.id)])


import uuid # Ce module est nécessaire à la gestion des identifiants unique (RFC 4122) pour les copies des livres

class BookInstance(models.Model):
    """Cet objet permet de modéliser les copies d'un ouvrage (C'est à dire, qui peut être emprunté)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(verbose_name="Date retour", null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets Book dans la base de données."""
        return f'{self.id} ({self.book.title})'

