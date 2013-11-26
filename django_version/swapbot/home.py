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


from django.contrib.auth import authenticate, login

def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render_to_response('login_success.html', {"user":user})
        else:
            # Return a 'disabled account' error message
            return render_to_response('accound_disabled.html', {})
            #static pages?
    else:
        # Return an 'invalid login' error message.
        return render_to_response('invalid_login.html', {})   

@login_required
def my_donations(reqest):
  
