from django.urls import path, include
from .views import get_account, get_positions, create_order, order_history


urlpatterns = [
    path('account/', get_account),
    path('positions/', get_positions),
    path('create_order/', create_order),
    path('order_history/', order_history)
]