from django.db import models
from django.contrib.auth.models import User #cette classe User est déjà crée par Django
#Django à une notion de User c'est pour ca qu'on supprime la classe User qu'on avait crée'

class UserProfileInfo(models.Model): #class de référence au user
    user = models.OneToOneField(User, on_delete = models.CASCADE)
     #relation entre la class user et celle des Tweet mais dans un sens unique.
    #une seul user est associé à ses tweet 
    bio =  models.CharField(max_length=400)
    profile_pic = models.ImageField (upload_to = 'profile_pic', blank =True)

#class User(models.Model):
    #username = models.CharField(max_length=264, unique=True)
    #name = models.CharField(max_length=264, unique = False)
    #bio = models.CharField(max_length= 1000, unique = False)

    #def __repr__(self):
        #return "<User {}>".format(self.username)

    #def __str__(self):
        #return self.name

class Tweet(models.Model):
    text = models.CharField(max_length=140, unique = False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.text



