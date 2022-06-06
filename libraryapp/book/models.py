from unicodedata import category
from django.db import models
#DataFlair Models
class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=124)
    age=models.IntegerField()
    book= models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
