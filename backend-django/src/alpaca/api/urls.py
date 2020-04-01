from django.urls import path, include
from . import views


urlpatterns = [
    path('account/', views.get_account),
    path('positions/', views.get_positions)
]