from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Choice)
admin.site.register(People)

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','pub_date']
    list_filter = ['question_text']
    fieldsets =[
        (None,{'fields':['question_text']}),
        ('Date Info',{'fields':['pub_date']})
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question,QuestionAdmin)