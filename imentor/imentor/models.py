from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers
import datetime
import json
import time

class Tag(models.Model):
  name = models.CharField(max_length = 100)
  tag_id = models.AutoField(primary_key = True)

  def __str__(self):
    return self.name

class Message(models.Model):
  timestamp = models.DateTimeField('date sent')
  content = models.CharField(max_length = 1000)
  message_id = models.AutoField(primary_key = True)
  sender = models.ForeignKey(User, related_name="Sender")
  recipient = models.ForeignKey(User, related_name="Recipient")
  tag = models.ForeignKey(Tag)

  def __str__(self): #return human-readable object description
    return '%s %s' % (self.content)

  def __unicode__(self):
    return self.timestamp

  def create_message(self, request, user_id):
    sender = int(user_id)
    data = json.loads(request.body)

    try:
      if data['mentee_id']:
        rec_id = int(data['mentee_id'])
    except:
      rec_id = int(data['mentor_id'])
    if int(data['message_tag']) not in range(1, 8):
      tag = 'Other'
    else:
      tag = self.tag_dict[int(data['message_tag'])]

    message = Message(timestamp = datetime.datetime.now(),
                       content = data['content'],
                       sender_id = sender,
                       reciever_id = rec_id,
                       tag_id = tag)
    message.save()
    return json.dumps({'timestamp': str(message.timestamp)})

  def retrieve_by_tags(self, request, user_id):
    sender = int(user_id)
    data = json.loads(request.body)
    if int(data['message_tag']) not in range(1, 8):
      tag = 'Other'
    else:
      tag = self.tag_dict[int(data['message_tag'])]
    #Now check if the user is a pc or (Mentor / Mentee)
    try:
      mentee_id = data['mentee_id']
      mentor_id = data['mentor_id']
      pc = True
    except:
      pc = False
    if not pc:
      #Should return lists even of these are single objects.
      #This roughly translates to find all messages with this tag that you sent
      result_one = Message.objects.filter(sender_id = sender, tag_id = tag)
      #Now, find messages that you recived with this tag
      result_two = Message.objects.filter(reciever_id = sender,tag_id = tag)
    else:
      #Retrieve messages sent on this topic by mentor to mentee
      result_one = Message.objects.filter(sender_id = mentor_id, reciever_id=mentee_id, tag_id = tag)
      result_two = Message.objects.filter(sender_id = mentee_id, reciever_id=mentor_id ,tag_id = tag)
    total_result = list(result_one) + list(result_two)
    total_result = sorted(total_result, key = lambda ii : time.mktime(ii.timestamp.timetuple()))
    ret_list = list()
    for ii in total_result:
      ret_list.append({"timestamp" : str(ii.timestamp), "content" : ii.content, "sender" : ii.sender_id,
                       "reciever" : ii.reciever_id})
    return json.dumps(ret_list)

#allows us to create users within the auth module
class UserProxy:

  @classmethod
  def create_user(self, request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    user = User(username=username,
                         email=email,
                         first_name=first_name,
                         last_name=last_name
                         )
    user.set_password(password)
    user.save()

    user = authenticate(request)
    return user

  @classmethod
  def authenticate(self, request):
    username = request.POST['username']
    password = request.POST['password']

    return authenticate(username=username, password=password)

class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True)
  rating = models.IntegerField(default=0)
  school = models.CharField(max_length=255)

  def __str__(self):
    return '%s %s\'s profile' % (self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
