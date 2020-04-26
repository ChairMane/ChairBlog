from django.contrib import admin
from .models import Post, Category
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on')
	list_filter = ['created_on']

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Chair Blog Posts'
