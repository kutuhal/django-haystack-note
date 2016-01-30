from django.contrib import admin
from .models import *

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date', 'title', )

admin.site.register(Note, NoteAdmin)
