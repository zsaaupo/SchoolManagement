from django.contrib import admin
from django.urls import path, include
from .views import home, classes
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Zsa Admin"
admin.site.site_title = "Zsa Admin Portal"
admin.site.index_title = "Welcome to Zsa Researcher Portal"

urlpatterns = [
    path('', home),
    path('classes/', classes),
    path('admin/', admin.site.urls),
    path('students/', include("Students.urls")),
    path('settings/', include("Settings.urls")),
    path('teachers/', include("Teachers.urls")),
    path('facility/', include("Facility.urls")),
    path('api-auth/', include('rest_framework.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)