from django.urls import path
from core import views

urlpatterns = [
    path('', views.index),
    path('root', views.root),
    path('statement', views.statement),
]
