from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Question, Category
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


# Aqui comeca outra view, que mostra as perguntas de uma categoria

def categories_view(request):
    categories = Category.objects.all()
    for category in categories:
        category.num_questions = category.questions.count()
    return render(request, "categories.html", {"categories": categories})


def study_cards_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    question = category.questions.first()  # futuramente random ou em ordem

    result = None

    # Defina o tipo do input na view
    input_type = (
        "checkbox"
        if question.correct_choices().count() > 1
        else "radio"
    )

    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_choices")
        selected_choices = question.choices.filter(id__in=selected_ids)
        correct_choices = question.correct_choices()

        is_correct = set(selected_choices) == set(correct_choices)
        result = {
            "is_correct": is_correct,
            "correct_choices_text": ", ".join(
                [c.text for c in correct_choices]
            ),
            "explanation": question.explanation,
        }

    return render(request, "study_cards.html", {
        "category": category,
        "question": question,
        "result": result,
        "input_type": input_type,  # Passe para o template
    })
