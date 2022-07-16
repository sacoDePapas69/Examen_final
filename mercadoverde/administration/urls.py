from django.urls import path
from .views import crud, categories, create_category, delete_category, update_category, products, create_product, update_product, delete_product#, shippings, update_shipping, users, update_user
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('crud/', crud, name = 'crud'),
    path('categories/', categories, name = 'categories'),
    path('createCategory/', create_category, name = 'create_category'),
    path('updateCategory/<id>', update_category, name = 'update_category'),
    path('deleteCategory/<id>', delete_category, name = 'delete_category'),

    path('products/', products, name = 'products'),
    path('createProduct/', create_product, name = 'create_product'),
    path('updateProduct/<id>', update_product, name = 'update_product'),
    path('deleteProduct/<id>', delete_product, name = 'delete_product'),
    #path('shippings/', shippings, name = 'shippings'),
    #path('updateShipping/', update_shipping, name = 'update_shipping'),
    #path('users/', users, name = 'users'),
    #path('updateUsers/', update_user, name = 'update_user'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
