from django.db import models

# Create your models here.
# Presentation List
class Event(models.Model):
    name = models.CharField(max_length=100)             # Presentation title
    limit = models.IntegerField()                       # Attend number
    status = models.BooleanField()                      # Status
    address = models.CharField(max_length=200)          # Address
    start_time = models.DateTimeField('events time')    # Presentation date
    create_time = models.DateTimeField(auto_now=True)   #Create time (auto get)

    def __str__(self):
        return self.name

# Presentation guest
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)                          # relevance presentation
    realname = models.CharField(max_length=64)                                          # name
    phone = models.CharField(max_length=16)                                             # phone
    email = models.EmailField()                                                         # email
    sign = models.BooleanField()                                                        # sign status
    create_time = models.DateTimeField(auto_now=True)                                   # create time

class Meta:
    unique_together = ("event", "phone")

def __str__(self):
    return self.realname