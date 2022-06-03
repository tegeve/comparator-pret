
from django.urls import path, include

from . import views

app_name = 'scraper'
urlpatterns = [
    path('', views.SearchView.as_view(), name='lista_coduri'),
    # path('', views.SearchResultView.as_view(), name='cautare_index'),


]
