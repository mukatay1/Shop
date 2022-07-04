from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import (TemplateView,
                                  DetailView,
                                  )

from .services import (CandyService,
                       CandyRecentService
                       )

from .models import Candy


# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        candy_context = CandyService(self.request).execute()
        return context | candy_context


class CandyDetail(DetailView):
    model = Candy
    template_name = 'detail.html'
    slug_url_kwarg = 'candy_slug'
    context_object_name = 'candy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        candy_context = CandyRecentService(self.request).execute(self.object)
        return context | candy_context


class CandySearch(View):
    def get(self, request):
        candy = CandyService(request).get_filtered_candies()
        if candy:
            return redirect(reverse('candy_detail', kwargs={'candy_slug': candy.slug}))
        return render(request, '404.html')
