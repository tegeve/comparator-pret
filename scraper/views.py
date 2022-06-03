from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from comparator.scraper_magazine import ScraperAltexEmag
from scraper.models import Cautare


class SearchView(CreateView):
    model = Cautare
    template_name = 'altex_vs_emag/cautare_produs.html'
    fields = ['cod_produs']

    def get_success_url(self):
        cuvant_cautat = self.model.objects.get(id=self.object.id).cod_produs
        cautare = ScraperAltexEmag(cuvant_cautat)
        print("====================")
        print(cautare)
        print("====================")
        return reverse('scraper:lista_coduri')
#
#
class SearchResultView(ListView):

    model = Cautare
    template_name = 'altex_vs_emag/cautare_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=1)
    context_object_name = 'scraper:lista_coduri'

    def get_context_data(self, *args, **kwargs):
        data = super(SearchResultView, self).get_context_data(*args, **kwargs)
        cautare = ScraperAltexEmag(data)
        print(data)
        return cautare
