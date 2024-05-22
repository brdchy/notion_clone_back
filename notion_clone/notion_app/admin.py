from django.contrib import admin
from.models import Tag, Project, Doc

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creation_date', 'update_date')
    search_fields = ['tags__name']
    filter_horizontal = ('tags',)

@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'creation_date', 'update_date', 'file')
    search_fields = ['author__username', 'filepath']
    filter_horizontal = ('tags',)
