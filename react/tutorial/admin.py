from .models import Comment
from django.contrib import admin

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    """
