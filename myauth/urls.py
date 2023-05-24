from django.urls import path
from myauth.views import main_view

urlpatterns = [
    path("", main_view),
]
