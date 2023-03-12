from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('', include('contacts.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

]
