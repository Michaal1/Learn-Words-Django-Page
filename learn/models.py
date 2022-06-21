from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.contrib.auth.models import User






class Werb(models.Model):
    #Sloveso
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=0, related_name =  "werb", null=True)
    word = models.CharField(max_length=200)
    tri_os = models.CharField(max_length=200)
    minuly_cas = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    tries = models.IntegerField(default=0)
    date = models.DateTimeField('date published')

    
    def __str__(self):
        return self.word
        
class Word(models.Model):
    #Podstatne meno / Pridavne meno
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=0, related_name = "word", null=True)

    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    tries = models.IntegerField(default=0)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.word


    
