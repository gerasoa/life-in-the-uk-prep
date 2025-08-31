from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question
# from django.views import View


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


def flashcards(request):
    questions = (
        Question.objects
        .prefetch_related('choices')
        .filter(is_flashcard=True)
    )
    questions_json = [
        {
            'question': q.text,
            'answer': ', '.join(
                [c.text for c in q.choices.all() if c.is_correct]
            )
        }
        for q in questions
    ]
    return render(
        request,
        'flashcards.html',
        {'questions_json': questions_json}
    )
