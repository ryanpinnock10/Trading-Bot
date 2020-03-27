
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api_auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', include('alpaca.urls')),
    path('api/', include('alpaca.api.urls'))
]
