from django.shortcuts import render, redirect
from twitter_app.models import Tweet
from twitter_app.forms import UserForm, UserProfileInfoForm
import datetime

#def index(request):
    #tweets = Tweet.objects.all().order_by('-date')[:30]
  #return render(request, 'index.html', { 'tweets': tweets })

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST)
        profile_form = UserProfileInfoForm (data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #le user est devenu un obk-ject object
            user.save()

            profile = profile_form.save(comit = False) #save as an object mmais pas dans la databse
            profile.user = user

            #cheack to se server if there is a profil picture

            if 'profil_pic' in request.FILES:#is implemented, kind of dictionary
             profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else: 
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        #syntax pour faire tourner le template
        return render(request, 'signup.html', {
            'user_former' : user_form,
            'profile_form' : profile_form,
            'registered' : registered       
            })

#forms.NOM DE LA CLASS PROVENANT DE LA PAGE METHOD, 
#def latest_tweets(request):
    #last_tweets = {
     #'tweet' : Tweet.objects.all().order_by('-date')[:20],
     #}
    #return render(request, 'last_tweets.html', context=last_tweets)

def gets_all_tweets_of_user(user_id):
    all_tweets = {
    'tweet' : Tweet.objects.filter(user= user_id)
    }
    return all_tweets

def user_profile(request, user_id):
    pass
    #user = User.objects.get(id=user_id)
    #tweets = Tweet.objects.filter(user=user_id).order_by ('-date') [:5]
    #return render(request, 'user_profile.html', context=gets_all_tweets_of_user(user_id))

def create_tweet (request, user_id):
    pass
    #user = User.objects.get(id = user_id)
    #form = forms.TweetForm()

    ##form = forms.TweetForm (requets.POST)
        #if  form.is_valid():
        #   text = form.cleaned_data['text']
            #tweet = Tweet (text = text, user = user, date = datetime.datetime.now())
            #tweet.save()

            #return redirect('/twitter_app/')
#
        #return render (request, 'tweetform.html', {'form':form, 'user': user})


