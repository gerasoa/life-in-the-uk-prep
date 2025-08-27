# from . import views
from django.urls import path
from .views import FlashcardView

urlpatterns = [
    # path('', views.HomePage.as_view(), name='home'),
    path("", FlashcardView.as_view(), name="flashcards"),
]
