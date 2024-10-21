from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/index.html')
def service(request):
    return render(request,'myapp/service.html')
def contact(request):
    return render(request,'myapp/contact.html')
def about(request):
    return render(request,'myapp/about.html') 
