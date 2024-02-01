from django.urls import path
from . import views

app_name = "Shortener"

urlpatterns= [
 path("home/",views.home ,name = 'home'),
 path("send_data/", views.send_data,name= "send"),
 path("redirect_URL/",views.urlRedirect),
 path("<str:short_url>/",views.urlRedirect)
]