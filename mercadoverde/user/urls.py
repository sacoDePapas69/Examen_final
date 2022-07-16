from django.urls import path
from .views import register, access, LOG_OUT
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', register, name = 'register'),
    path('access/', access, name = 'access'),
    path('logout', LOG_OUT, name = 'logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
