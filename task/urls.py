from django.urls import path

from . import views

urlpatterns =[
    path('', views.home, name = 'task'),
    path('update/<str:pk>/',  views.update, name='update'),
    path('delete/<str:pk>/',  views.delete, name='delete')
]