from . import views
from django.urls import path
urlpatterns = [
    path('',views.home, name='home'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about,name='about'),
]