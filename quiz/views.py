from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Question, Category
import json


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


# Aqui comeca outra view, que mostra as perguntas de uma categoria

def categories_view(request):
    categories = Category.objects.all()
    for category in categories:
        category.num_questions = category.questions.count()
    return render(request, "categories.html", {"categories": categories})


def study_cards_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = list(category.questions.prefetch_related('choices').all())
    questions_json = json.dumps([
        {
            "question": q.text,
            "choices": [
                {"id": c.id, "text": c.text, "is_correct": c.is_correct}
                for c in q.choices.all()
            ],
            "multiple": q.correct_choices().count() > 1,
            "explanation": q.explanation,
        }
        for q in questions
    ])
    return render(request, "study_cards.html", {
        "category": category,
        "questions_json": questions_json,
    })
