from django.urls import path
from . import views

urlpatterns = [

    path('', views.UserRequestListView.as_view(), name='home'),
    path('create/', views.create, name='create')
]
