from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from trips import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.trip_list, name='trip_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)