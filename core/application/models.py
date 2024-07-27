from django.db import models


class Joke(models.Model):
    setup = models.TextField()
    punch_line = models.TextField()
    joke_type = models.CharField(max_length=255, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.setup


