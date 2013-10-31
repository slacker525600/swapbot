from swapbot.models import Items
from django.shortcuts import render_to_response

def thank_you(request):
  return render_to_response('thanks.html', {})
#def thanks(request):
#  return render_to_response('thanks.html', {})

def index(request):
  aItems = Items.objects.all()
  #should I pass the actual items into the homepage template or the json
  #serializers.serialize('json', Items.objects.all())
  #or aItems = Items.objects.filter(visibal__equals=True) #or something.
  return render_to_response('homepage.html', {'aItems':aItems})

def request(request):
  return render_to_response('request.html', {})

def sign_up(request):
  return render_to_response('sign_up.html', {})

def json(request):
  cClassToUse = Object
  if 'items' in request:
    cClassToUse = Items
  return serializers.serialize('json', cClassToUse.objects.all())

