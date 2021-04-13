from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'account/main.html')

#def products(request):
    #return HttpResponse('Products')

#def customer(request):
    #return HttpResponse('Customer')