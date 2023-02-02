from django.contrib import admin

from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "comment", "status"]
    list_display_links = ["id", "name"]

admin.site.register(ToDo, ToDoAdmin)
