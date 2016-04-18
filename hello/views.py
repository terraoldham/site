from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    #r = requests.get('http://httpbin.org/status/418')
    #print r.text
    #return HttpResponse('<pre>' + r.text + '</pre>')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def contact(request):
    return render(request, 'contact.html')

def submit_contact(request):
    Contact.objects.create(first_name=request.POST['first_name'])
    Contact.objects.create(last_name=request.POST['last_name'])
    Contact.objects.create(email_address=request.POST['email_address'])
    Contact.objects.create(phone_number=request.POST['phone_number'])
    contact_information = Contact()
    contact_information.save()
    all_contact_information = Contact.objects.all()
    return render(request, 'submit_contact.html', {'all_contact_information': all_contact_information})


