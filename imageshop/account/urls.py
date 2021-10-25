from django.urls import path
from . import views

urlpatterns = [
    
         path('signup',views.signup, name='signup'),
         path('signin',views.signin, name='signin'),
         path('logout',views.logout, name='logout'),
         path('search',views.search, name='search'),
         path('pay',views.pay, name='pay'),
         path('cart',views.cart, name='cart'),

]