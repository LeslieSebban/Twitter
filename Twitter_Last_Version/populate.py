#pip install Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Twitter_Last_ Version.settings')
import django
django.setup()


# Fake populate script
from faker import Faker 
from twitter_app.models import UserProfileInfo, Tweet

fakegen = Faker()

def populate():

 username  = fakegen.user_name()
  name = fakegen.name()
  bio = fakegen.text()


def populate():
  users = []
  for user in range(20):
    user = create_user()
    for tweet in range(50):
      tweet = create_tweet(user)


if __name__ == '__main__':
  print('Starting to populate...')
  populate()
  print('Finished populating!')












