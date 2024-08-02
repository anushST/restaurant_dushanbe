"""URL configuration for backend project."""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .admin_site import my_admin_site

urlpatterns = [
    path('admin/', my_admin_site.urls),
    path('api/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
