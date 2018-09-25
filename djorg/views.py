from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie


class Home(TemplateView):
    template_name = 'base.html'