from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question,Choice,User,Student,Permission

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    # (None, {'fields': ['question_text']}),
    # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'per_method','describe')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Permission,PermissionAdmin)