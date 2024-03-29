from django.contrib import admin
from .models import Question, Choice, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields':['question_text']}),
            ('Date information', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['pub_date', 'question_text', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote)
