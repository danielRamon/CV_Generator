from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.template import loader
from .models import Identity


# Create your views here.

def my_view(request, dni):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        identity = Identity.objects.get(dni=dni)
        template = loader.get_template('curriculum/curriculum_page.html')
        context = {
            'identity': identity,
        }
        return HttpResponse(template.render(context, request))
    else:
        # Return an 'invalid login' error message.
        return HttpResponse(False)

def showCurriculum(request, dni):
    identity = Identity.objects.get(dni=dni)
    template = loader.get_template('curriculum/curriculum_page.html')
    context = {
        'identity': identity,
    }
    return HttpResponse(template.render(context, request))
