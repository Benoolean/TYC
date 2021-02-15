from django.shortcuts import render
from django.views import View


class LandingIndexView(View):
    template_name = 'landing/index.html'

    def get(self, request):
        return render(request, self.template_name)



