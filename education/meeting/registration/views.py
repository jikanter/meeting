# django views dealing with user registration and interaction

import urllib
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def signup(request):
    qs = request.GET.copy()
    user = qs.get('u', None)
    if not user:
        return HttpResponseRedirect('/register/user/create')
    return HttpResponseRedirect('/r/Meeting/?%s' % urllib.urlencode({'u': user}))
    
def createuser(request):
    return render_to_response('adduser.html', {'flash': 'Sign up'}, context_instance=RequestContext(request))
    
def adduser(request):
    qs = request.POST.copy()
    if not qs.has_key('django-username'):
        return HttpResponseRedirect('/register/createuser')
    u = User(username=qs['django-username'], 
             first_name=qs['django-firstname'], 
             last_name=qs['django-lastname'], 
             email=qs['django-email'])
    u.set_password(qs['django-password'])
    u.save()
    return render_to_response('adduser.html', {'u': u, 'flash': 'User Created'}, 
                              context_instance=RequestContext(request))
                              
def loginuser(request):
    qs = request.POST.copy()
    # if we aren't given a username and password, for the visitor to log in
    if (not qs.has_key('django-username')) or (not qs.has_key('django-password')):
        return render_to_response('loginuser.html', {'flash': 'Log in'},
                                  context_instance=RequestContext(request))
    try:
        u = User.objects.get(username=qs['django-username'])
    except ObjectDoesNotExist:
        return render_to_response('loginuser.html', {'flash': 'User does not exist. Please try again'},
                                  context_instance=RequestContext(request))
    if u.password == qs['django-password']:
        request.session['user_id'] = u.id
        return render_to_response('Meeting.html', {'flash': 'logged in'},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('loginuser.html', {'flash': '''You're username and password did not match. please log in'''},
                                  context_instance=RequestContext(request))

def logoutuser(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render_to_response('loggedout.html', {'flash': '''You're logged out'''},
                              context_instance=RequestContext(request))

    

    