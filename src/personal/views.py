from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# Create your views here.
def home(request):
    context={}
    template='personal.html'
    return render(request,template,context)