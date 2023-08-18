from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    review = models.TextField()
    def __str__(self):
        return self.name+" / "+self.review
    
class Movie(models.Model):
    name = models.CharField(max_length=122)    
    released = models.DateField()    
    desc = models.CharField(max_length=500)       
    genre1 = models.CharField(max_length=500) 
    genre2 = models.CharField(max_length=500) 
    country = models.CharField(max_length=500) 
    downloadlDIRECTlink= models.CharField(max_length=500) 
    watchmovielink = models.CharField(max_length=500) 
    movielinkonwebsite = models.CharField(max_length=500,null=True) 
    trendingORHighImdbratedORLatestORNone = models.CharField(max_length=500,null=True) 
    imdb = models.FloatField() 
    # file = models.FileField()           
    image_file = models.FileField()         
    def __str__(self):
        return self.name
          