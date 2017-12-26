from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date', 'question_text']

    search_fields = ['pub_date']

    fieldsets = [
        ('Basic information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
