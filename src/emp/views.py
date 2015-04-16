from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from  django.db import models
from models import PersonTest

# Create your views here.
def emp(request):
    people = PersonTest.objects.all()
    t = loader.get_template('employee.html')
    c = Context({'people': people})
    return HttpResponse(t.render(c))


def insert(request):
    if request.method == 'POST':
        p = PersonTest(
            name=request.POST['name'],
            phone=request.POST['phone'],
            age=request.POST['age']
        )
        p.save()

    t = loader.get_template('insert.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))


def edit(request, person_id):
    p = PersonTest.objects.get(pk=person_id)
    if request.method == 'POST':
        p.name = request.POST['name']
        p.phone = request.POST['phone']
        p.age = request.POST['age']
        p.save()
    t = loader.get_template('insert.html')
    c = RequestContext(request, {
        'person': p
    })
    return HttpResponse(t.render(c))


def delete(request, person_id):
    p = PersonTest.objects.get(pk=person_id)
    p.delete()
    return HttpResponseRedirect('/emp')