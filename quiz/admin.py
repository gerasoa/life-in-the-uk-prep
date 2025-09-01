from django.contrib import admin
from .models import Question, Choice, Category


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2  # show 2 extra empty fields in the admin


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "question_type")
    inlines = [ChoiceInline]    


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
