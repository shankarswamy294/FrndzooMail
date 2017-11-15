# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from emailapp.models import Person,Compose
from emailapp.serializers import PersonSerializer,ComposeSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic,View
from  django.shortcuts  import render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect




@csrf_exempt
def persondetail(request):
    if request.method == 'GET':
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return render(request, "emailapp/person.html", {'serializer': serializer})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/add')
    else:
        form = UserCreationForm()
    return render(request, 'emailapp/signup.html', {'form': form})


class Home(LoginRequiredMixin,View):
    def get(self, request):
        return render_to_response('emailapp/home.html')

class Main(View):
    def get(self, request):
        return render_to_response('emailapp/main.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)

@csrf_exempt
def inbox(request):
    if request.method == 'GET':
        username = None
        if request.user.is_authenticated():
            username = request.user.username

        snippets = Compose.objects.filter(sendto__name=username)
        print (Compose.objects.filter(sendto__email="shankarswamy294@gmail.com"))
        serializer = ComposeSerializer(snippets, many=True)
        return render(request, "emailapp/inbox.html", {'serializer': serializer})

    if request.method == 'POST':
        return redirect('/inbox')

from django.views import View
from django.views.generic.edit import CreateView,DeleteView

class Add_upload(CreateView,View):
    model = Person
    context_object_name = "all_upload"
    fields = ["name","email"]
    success_url = "/home"


class composeview(CreateView,View):
    model = Compose
    context_object_name = "all_upload"
    fields = ["fromemail","sendto","subject","content"]
    success_url = "/home"

class Delete_mail(DeleteView):
    model = Compose
    context_object_name = "all_upload"
    template_name = "emailapp/mail_delete.html"
    success_url = '/inbox'
