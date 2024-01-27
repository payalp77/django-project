from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Membernew
from django.views.decorators.csrf import csrf_exempt
from .forms import Memberform

# create your views here

def all_members(request):
    member_list = Membernew.objects.all().values()
    context = {
        'member_list':member_list
    }
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render(context,request))
   
def contacts(request):
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render())
    


def detail(request, id):
    mymember = Membernew.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
        'mymember':mymember
        }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def add_newmembers(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname',)
        lastname = request.POST.get('lastname',)
        rollno = request.POST.get('rollno',)
        phoneno = request.POST.get('phoneno',)
        image = request.FILES['image']
        membernew = Membernew(firstname=firstname,lastname=lastname,rollno=rollno,phoneno=phoneno,image=image)
        membernew.save()
    template = loader.get_template('add_newmembers.html')
    return HttpResponse(template.render())



def update(request,id):
    member = Membernew.objects.get(id=id)
    form = Memberform(request.POST,instance=member)
    if form.is_valid():
        form.save()
        template = loader.get_template('add_newmembers.html')
        return HttpResponse(template.render())
    return render(request,'update.html',{'form':form,'member':member})

@csrf_exempt
def delete(request,id):
    if request.method == 'POST':
        member = Membernew.objects.get(id=id)
        member.delete()
        template = loader.get_template('all_members.html')
        return HttpResponse(template.render())
    return render(request,'delete.html')

    