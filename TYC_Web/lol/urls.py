from django.urls import path

from . import views
from lol.views import AccountView

urlpatterns = [
    path('', AccountView.as_view())
]