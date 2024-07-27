import json

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.views import View
from django.views.generic import TemplateView

from core.application.models import Joke
from core.settings import BASE_DIR

""" HOME PAGE LOGIC HERE """


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)
        context['joke'] = Joke.objects.filter(is_active=True).order_by('?').first()
        return context


class GetJokeJsonView(View):

    def get(self, request):
        joke = Joke.objects.filter(is_active=True).order_by('?').first()
        if joke:
            data = {
                'setup': joke.setup,
                'punchline': joke.punch_line,
                'id': joke.id,
                'success': 1,
            }
        else:
            data = {
                'success': 0
            }
        return JsonResponse(
            data=data, safe=False
        )


""" URL CONFIGURATION """


urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('json/get/joke/', GetJokeJsonView.as_view(), name='Json'),
    path('admin/', admin.site.urls),
]
