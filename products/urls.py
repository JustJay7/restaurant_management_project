from django.urls import path
from .views import ItemView, MenuView

urlpatterns = [
    path('items/', ItemView.as_view()),
    path('menu/', MenuView.as_view()),
]