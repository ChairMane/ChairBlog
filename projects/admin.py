from django.contrib import admin
from projects.models import Projects
from markdownx.admin import MarkdownxModelAdmin

class ProjectsAdmin(admin.ModelAdmin):
	list_display = ('title', 'project_link')

admin.site.register(Projects, ProjectsAdmin)

