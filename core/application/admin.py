from django.contrib import admin
from core.application.models import Joke


class JokeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'setup', 'is_active', 'created_on'
    ]


admin.site.register(Joke, JokeAdmin)
