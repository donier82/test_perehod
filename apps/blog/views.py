
# Create your views here.
from django.shortcuts import render
#from .models import Geeks

# Create your views here.
def index(request):
    #geeks = Geeks.objects.latest('id')
    return render(request, 'index.html', locals())

