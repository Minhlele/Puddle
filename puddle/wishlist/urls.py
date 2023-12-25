from django.urls import path

from . import views
app_name = 'wishlist'
urlpatterns = [   
    path('',views.index,name="index"),
    path('<int:item_id>/remove_from_wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
]