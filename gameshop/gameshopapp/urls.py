from django.urls import path
from gameshopapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('create_product', views.create_product),
    path('read_product', views.read_product),
    path('delete_product/<rid>', views.delete_product),
    path('update_product/<rid>', views.update_product),
    path('register', views.user_register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('create_cart/<rid>', views.create_cart),
    path('readcart', views.read_cart),
    path('delete_cart/<rid>', views.delete_cart),
    path('update_cart/<rid>/<q>', views.update_cart),
    path('create_orders/<rid>', views.create_orders),
    path('read_orders', views.read_orders),
    path('create_review/<rid>', views.create_reviews),
    path('read_product_detail/<rid>', views.read_product_detail),
    path('forgot_password', views.forgot_password),
    path('otp_verification', views.otp_verification),
    path('newpassword', views.new_password)
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

