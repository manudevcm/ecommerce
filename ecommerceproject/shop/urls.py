from django.urls import path, include
from . import views
app_name='shop'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('shop/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]