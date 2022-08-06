from django.urls import path
from contact import views

urlpatterns = [
    path('', views.contact_page, name='contact'),
    path('appointment', views.appointment, name='appointment'),
]
