from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('add/', views.add_note, name='add_note'),

    path('delete/<int:id>/', views.delete_note, name='delete_note'),

    path('update/<int:id>/', views.update_note, name='update_note'),

]