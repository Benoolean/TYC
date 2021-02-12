from django.views import generic
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .models import RiotAccountModel

@method_decorator(login_required, name='dispatch')
class AccountView(View):
    model = RiotAccountModel
    template_name = 'base_generic.html'

    def get(self, request):
        return render(request, self.template_name) 


# class AccountView(LoginRequiredMixin, generic.ListView):
#     model = RiotAccountModel
#     template_name = 'base_generic.html'

#     def get(self, request):
#         return render(request, self.template_name)