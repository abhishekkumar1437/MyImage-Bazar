from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('search',views.search, name='search'),
    path('image_like/',views.image_like, name='image_like'),
    path('imgresults/<int:id>/',views.imgresults, name='imgresults'),
    path('category/<int:pkid>/',views.show_category,name='show_category'),
    
]