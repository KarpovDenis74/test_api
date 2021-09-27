from django.contrib import admin

from api.models import Answer, Question, QuestionType, Survey, Result


class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'type', 'survey', )
    search_fields = ('text',)
    list_filter = ('survey',)
    empty_value_display = '-пусто-'


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_start', 'date_end', 'description', )
    search_fields = ("name",)
    list_filter = ("date_start", "date_end", )
    empty_value_display = "-пусто-"


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'text', )
    search_fields = ("question",)
    list_filter = ("text", )
    empty_value_display = "-пусто-"


class ResultAdmin(admin.ModelAdmin):
    list_display = ('pk', 'interviewee', 'answer',
                    'question', 'survey', 'your_answer')
    search_fields = ("your_answer",)
    list_filter = ("interviewee", )
    empty_value_display = "-пусто-"


admin.site.register(QuestionType, QuestionTypeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)
