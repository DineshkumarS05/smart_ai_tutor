from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('modify-text/', views.modify_text, name='modify-text'),
]