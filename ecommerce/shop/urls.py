from django.urls import path
from . import views

urlpatterns = [
    # Product URLs
    path('', views.product_list, name='product-list'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),
    
    # Cart URLs
    path('cart/', views.cart_view, name='cart-view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    
    # Order URLs
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order-history'),
    path('orders/<int:order_id>/', views.order_detail, name='order-detail'),
    
    # Authentication URLs
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
]