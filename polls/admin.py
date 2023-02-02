from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    fields = ['question_text', 'pub_date']
    readonly_fields = ['pub_date']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']
    fields = ['question', 'choice_text', 'votes']
