from django.urls import path
from .views import home, watch_products, watch_product, about, api
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name = 'home'),
    path('products', watch_products, name = 'watch_products'),
    path('product/<id>', watch_product, name = 'watch_product'),
    path('about_us/', about, name = 'about'),
    path('currencies/', api, name = "money")

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
