from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View
class Home(View):
    @staticmethod
    def get(request):
        return render(request, 'home.html')
