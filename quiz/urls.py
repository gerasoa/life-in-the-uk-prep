# from . import views
from django.urls import path
from .views import flashcards

urlpatterns = [
    # path('', views.HomePage.as_view(), name='home'),
    path("", flashcards, name="flashcards"),
]
