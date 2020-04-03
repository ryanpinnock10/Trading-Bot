from django.urls import path, include
from .views import get_account, get_positions
import views


urlpatterns = [
    path('account/', views.get_account),
    path('positions/', views.get_positions)
]