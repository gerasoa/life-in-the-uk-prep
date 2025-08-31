from django.db import models


class Question(models.Model):
    QUESTION_TYPES = [
        ("MC", "Multiple Choice"),
        ("YN", "Yes/No"),
    ]

    text = models.TextField("Question text")

    question_type = models.CharField(
        max_length=2, choices=QUESTION_TYPES, default="MC"
    )

    is_flashcard = models.BooleanField(
        default=True,
        help_text="Use this question in flashcards?"
    )  

    def __str__(self):
        return self.text[:50]  # Show only first 50 characters

    def correct_choices(self):
        """Return only the correct answers (for flashcards)."""
        return self.choices.filter(is_correct=True)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )

    text = models.CharField(max_length=600)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"
