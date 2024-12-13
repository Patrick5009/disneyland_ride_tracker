from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='rides'),
    path('update_ride/<str:pk>/', views.updateRide, name="update_ride"),
    path('delete/<str:pk>/', views.deleteRide, name="delete"),

]
