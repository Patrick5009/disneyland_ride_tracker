from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('update_ride/<str:pk>/', views.updateRide, name="update_ride"),

]