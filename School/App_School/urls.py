from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.open_index, name='open_index')   

]