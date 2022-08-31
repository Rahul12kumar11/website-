from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import View
from .models import Message
# Create your views here.

def index(request):
    if request.method == 'POST':
        new_name = request.POST['name']
        new_phone = int(request.POST['phone'])
        new_email = request.POST['email']
        new_message = request.POST['message']

        add_message = Message(name = new_name,phone = new_phone,email = new_email,message = new_message)
        add_message.save()
        redirect('/')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def overview(request):
    return render(request,'overview.html')
def product(request):
    return render(request,'product.html')
def service(request):
    return render(request,'service.html')
