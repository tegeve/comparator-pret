
from django.urls import path, include

from . import views

app_name = 'scraper'
urlpatterns = [
    path('', views.SearchView.as_view(), name='search_view'),
    path('rezultat/', views.ResultView.as_view(), name="results_view"),
    path('<int:pk>/delete/', views.delete_product, name='sterge'),
    path('<int:pk>/rezultat/', views.activate_product, name='activeaza'),
    path('produse_inactive', views.ProductInactiveView.as_view(), name='produse_inactive'),
]
