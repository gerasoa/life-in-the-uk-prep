from . import views
from django.urls import path
from .views import flashcards

urlpatterns = [
    # path('', views.HomePage.as_view(), name='home'),
    path("", views.categories_view, name="categories"),
    path("flashcards/", flashcards, name="flashcards"),
    path("categories/", views.categories_view, name="categories"),
    path(
        "categories/<int:category_id>/study/",
        views.study_cards_view,
        name="study_cards",
    ),
]
