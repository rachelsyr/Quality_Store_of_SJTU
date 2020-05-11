from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name',  'shop', 'created_time']
    fields = ['name',  'text', 'shop']


admin.site.register(Comment, CommentAdmin)
