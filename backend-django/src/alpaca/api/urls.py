from django.urls import path, include
from .views import get_account, get_positions, create_order


urlpatterns = [
    path('account/', get_account),
    path('positions/', get_positions),
    path('create_order/', create_order.as_view())
]