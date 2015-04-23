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
    c = RequestContext(request, {
        'people': people
    })
    return HttpResponse(t.render(c))



def insert(request):
    if request.method == 'POST':
        p = PersonTest(
            name=request.POST['name'],
            Mobile=request.POST['mobile'],
            Empid=request.POST['empid'],
            department=request.POST['department'],
            designation=request.POST['designation'],
            dob=request.POST['dob'],
            Address=request.POST['address'],
            EmgContact=request.POST['emgContact'],
            bloodgroup=request.POST['bloodgroup'],
            email=request.POST['email'],
        )
        p.save()
        return HttpResponseRedirect('/emp')
    t = loader.get_template('insert.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))


def edit(request, person_id):
    p = PersonTest.objects.get(pk=person_id)
    if request.method == 'POST':
        p.name=request.POST['name']
        p.Mobile=request.POST['mobile']
        p.Empid=request.POST['empid']
        p.department=request.POST['department']
        p.designation=request.POST['designation']
        p.dob=request.POST['dob']
        p.Address=request.POST['address']
        p.EmgContact=request.POST['emgContact']
        p.bloodgroup=request.POST['bloodgroup']
        p.email=request.POST['email']


        p.save()
        return HttpResponseRedirect('/emp')
    t = loader.get_template('insert.html')
    c = RequestContext(request, {
        'person': p
    })
    return HttpResponse(t.render(c))


def delete(request, person_id):
    p = PersonTest.objects.get(pk=person_id)
    p.delete()
    return HttpResponseRedirect('/emp')