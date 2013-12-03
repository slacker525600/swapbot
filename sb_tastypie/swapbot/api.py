from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from swapbot.models import Item, UserProfile, Donor, Donation
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.throttle import CacheDBThrottle
from django.db import models
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)

from tastypie.validation import Validation


class AwesomeValidation(Validation):
    def is_valid(self, bundle, request=None):
        print "======================"
        print request
        print "======================"
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = {}

        for key, value in bundle.data.items():
            if not isinstance(value, basestring):
                continue

            if not 'awesome' in value:
                errors[key] = ['NOT ENOUGH AWESOME. NEEDS MORE.']

        return errors

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        
class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'
        allowed_methods = ['get']
        authentication = SessionAuthentication()
        
class UserProfile(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'userProfile'
        authorization = Authorization()
        
class DonorResource(ModelResource):
    class Meta:
        queryset = Donor.objects.all()
        resource_name = 'doner'
        authorization = Authorization()
        
class DonationResource(ModelResource):
    class Meta:
        queryset = Donation.objects.all()
        resource_name = 'donation'
        authorization = Authorization()
        authentication = Authentication()
        filtering = {"size": ('exact', 'startswith',),}
        validation = AwesomeValidation()
        throttle = CacheDBThrottle(throttle_at=200)
        
