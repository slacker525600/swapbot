from django.db import models
from django.contrib.auth.models import User
# import time
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# @receiver(post_save, sender=User)
# def my_callback(sender, **kwargs):
#     print("sleep....")  
#     time.sleep(5)
#     print("post_save finished!") 
    
    
    
class Item(models.Model):      
    TYPE = (
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Child', 'Child'),
    )
    item = models.CharField(max_length=50, null=False, primary_key=True)
    mwc = models.CharField(max_length=10, choices=TYPE)
    image = models.ImageField(upload_to='static/img')
    estimatedPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __unicode__(self):  
        return self.item
      
class OpenHour(models.Model):  
    open_time = models.TimeField(null=False)
    close_time = models.TimeField(null=False)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)
    
    def __unicode__(self):  
        return self.open_time.__str__() + " - " + self.close_time.__str__()

  
class Location(models.Model):
    lat = models.CharField(max_length=32, null=False)
    long = models.CharField(max_length=32, null=False)
    street_addr = models.CharField(max_length=512, null=False, primary_key=True)
    zip = models.CharField(max_length=6, null=False)
    openHours = models.OneToOneField(OpenHour)
    
    def __unicode__(self):  
        return self.street_addr
      
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.user.__str__()

class Donor(models.Model):
    profile = models.OneToOneField(UserProfile)
    def __unicode__(self):  
        return self.profile.__str__()

  
    
class SocialWorker(models.Model):
    profile = models.OneToOneField(UserProfile)
    locatons = models.OneToOneField(Location)
    def __unicode__(self):  
        return self.profile.__str__()
       
class Recipient(models.Model):
    profile = models.OneToOneField(UserProfile)
    socialWorker = models.ForeignKey(SocialWorker)
    def __unicode__(self):  
        return self.profile.__str__()
    
    
class DropSchedule(models.Model):
    schedule = models.DateTimeField()
    dropped = models.BooleanField(default=False)
    missed = models.BooleanField(default=False)
    socialWorker = models.ForeignKey(SocialWorker)
    def __unicode__(self):  
        return self.id.__str__()
        
class Donation(models.Model):
    SIZE = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    donor = models.ForeignKey(Donor)
    item = models.ForeignKey(Item)
    size = models.CharField(max_length=10, null=True, choices=SIZE)
    created = models.DateTimeField(auto_now_add=True)    
    dropSchedule = models.ForeignKey(DropSchedule, blank=True, null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.id.__str__() + " | " + self.donor.__str__() + " | " + self.item.__str__() + " | " + self.created.__str__()

    
class Request(models.Model):
    SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    item = models.ForeignKey(Item)
    size = models.CharField(max_length=1, null=True, choices=SIZE)
    recipient = models.ForeignKey(Recipient)
    socialWorker = models.ForeignKey(SocialWorker)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.id.__str__() + " | " + self.socialWorker.__str__() + " | " + self.item.__str__() +  " | " + self.recipient.__str__()
    
class Swap(models.Model):
    donation = models.ForeignKey(Donation)
    request = models.ForeignKey(Request)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(blank=True,null=True)
    def __unicode__(self):
        return self.id.__str__() + " | " + self.donation.donor.__str__() + " --> " + self.request.recipient.__str__()
    
