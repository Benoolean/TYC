from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import TournamentModel


@method_decorator(login_required, name='dispatch')
class LeagueIndexView(DetailView):
    model = TournamentModel
    template_name = 'lol/index.html'

    queryset = model.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'tournament_list' : self.queryset}) 


@method_decorator(login_required, name='dispatch')
class RiotAccountView(LeagueIndexView):
    model = RiotAccountModel
    template_name = 'lol/index.html'

    queryset = model.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'tournament_list' : self.queryset}) 


# class AccountView(LoginRequiredMixin, generic.ListView):
#     model = RiotAccountModel
#     template_name = 'base_generic.html'

#     def get(self, request):
#         return render(request, self.template_name)