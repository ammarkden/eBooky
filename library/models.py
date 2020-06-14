from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    numberOfBooks = models.IntegerField(blank = True, null = True)
    def __str__(self):
        return f" Category: {self.categoryName}"


class Book(models.Model):
    bookName = models.CharField(max_length= 100)
    bookAuthor = models.CharField(max_length= 100)
    bookPages = models.IntegerField()
    bookPrice = models.FloatField()
    bookISBN = models.IntegerField(blank = True, null = True)
    bookDetails = models.TextField(blank = True, null = True)
    bookWiki = models.TextField(blank = True, null = True)
    bookCover =  models.ImageField(upload_to='library', blank =True, null =True)
    bookLink = models.CharField(max_length=200, blank =True, null=True)
    amazonLink = models.CharField(max_length= 400, blank =True, null =True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank =True, null =True, related_name = 'Cat_Books')
    def __str__(self):
         return f" Book name: { self.bookName}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileIcon =  models.ImageField(upload_to='library', blank=True, null=True)
    booklist = models.ManyToManyField(Book, blank = True, related_name = 'listbooks')
    def __str__(self):
        return f" username {self.user}"
    




    

