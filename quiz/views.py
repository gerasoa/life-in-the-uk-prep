from django.shortcuts import render, get_object_or_404, redirect
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
    questions = list(category.questions.all())
    
    question_idx = int(request.GET.get("q", 0))
    if question_idx >= len(questions):
        # Se não há mais questões, redirecione para categories
        return redirect("categories")

    question = questions[question_idx] if questions else None

    result = None
    selected_ids = []

    input_type = "checkbox" if question and question.correct_choices().count() > 1 else "radio"

    # Se o botão "Finalizar" foi pressionado
    if request.method == "GET" and "finish" in request.GET:
        return redirect("categories")

    # Se o botão "Next" foi pressionado, avance para a próxima questão
    if request.method == "GET" and "next" in request.GET:
        next_idx = question_idx + 1
        return redirect(f"{request.path}?q={next_idx}")

    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_choices")
        selected_choices = question.choices.filter(id__in=selected_ids)
        correct_choices = question.correct_choices()

        is_correct = set(selected_choices) == set(correct_choices)
        result = {
            "is_correct": is_correct,
            "correct_choices_text": ", ".join([c.text for c in correct_choices]),
            "explanation": question.explanation,
        }

    # Verifica se é a última questão
    is_last_question = (question_idx == len(questions) - 1)

    return render(request, "study_cards.html", {
        "category": category,
        "question": question,
        "result": result,
        "input_type": input_type,
        "selected_ids": selected_ids,
        "is_last_question": is_last_question,
        "question_idx": question_idx,
    })
