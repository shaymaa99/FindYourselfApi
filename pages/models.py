from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    url=models.CharField(max_length=10000)
    def __str__(self):
        return self.name

class Activity(models.Model):
   type=models.ForeignKey(Category,on_delete=models.CASCADE)
   hoppy_title=models.CharField(max_length=100)
   url=models.CharField(max_length=1000)
   def __str__(self):
        return self.hoppy_title
class Book(models.Model):
    title=models.CharField(max_length=1000)
    book_cover_url=models.CharField(max_length=1000)
    url=models.CharField(max_length=1000)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Video(models.Model):
    url=models.CharField(max_length=1000)
    type=models.CharField(max_length=100)
class app_Question(models.Model):
    question=models.CharField(max_length=1000000)
class Data_of_Category(models.Model):
      description=models.TextField()