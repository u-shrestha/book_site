from django.db import models
from multiselectfield import MultiSelectField

class Book_detail(models.Model):
    btitle = models.CharField(max_length=100)
    GENRE_CHOICES = (
        ('fi', 'Fiction'),
        ('nf', 'Non-fiction'),
        ('cl', 'Classic'),
        ('ro', 'Romance'),
        ('fa', 'Fantasy'),
        ( 'my', 'Mystery'),
        ( 'co', 'Comics'),
        ( 'gn', 'Graphic-novel'),
        ( 'sf', 'Science-fiction'),
        ('hi', 'History'),
        ( 'bi', 'Biography'),
        ( 'su', 'Superhero'),
        ('th', 'Thriller'),
        ('ct', 'Contemporary'),
        ('ad', 'Adventure')
    )
    bgenre = MultiSelectField(choices=GENRE_CHOICES)
    bauthor = models.CharField(max_length=100)
    bisbn =  models.CharField(max_length=100, primary_key=True, blank=False)
    bpages = models.CharField(max_length=30)
    bpublished = models.CharField(max_length=80)
    bpublished_by = models.CharField(max_length=100)
    bcover = models.ImageField(upload_to="book_cover")
    bo_lang = models.CharField(max_length=50,blank=True)
    bdesc = models.TextField(blank=True)

    def __str__(self):
        return self.btitle



