from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question
from django.views import View


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


class FlashcardView(View):
    template_name = "flashcards.html"

    def get(self, request):
        questions = Question.objects.all()
        return render(request, self.template_name, {"questions": questions})
