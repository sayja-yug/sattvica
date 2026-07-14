from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.demo, name='demo'),
    path('results/<int:pk>/', views.results, name='results'),
]
