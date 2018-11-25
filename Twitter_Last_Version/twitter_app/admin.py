from django.contrib import admin
from twitter_app.models import Tweet, UserProfileInfo

#admin.site.register(User) #register = afficher dans l'admin
admin.site.register(Tweet)
admin.site.register(UserProfileInfo) 
