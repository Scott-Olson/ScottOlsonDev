from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Blog, Tag

# Register your models here.

admin.site.register([Blog, Tag], MarkdownxModelAdmin)