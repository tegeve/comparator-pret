

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from comparator.scraper_magazine import ScraperAltexEmag
from scraper.models import Produse


class SearchView(LoginRequiredMixin, CreateView):
    model = Produse
    template_name = 'altex_vs_emag/cautare_produs.html'
    fields = ['cod_produs']

    def get_success_url(self):
        cuvant_cautat = self.model.objects.get(id=self.object.id).cod_produs
        scrapper = ScraperAltexEmag(cuvant_cautat)
        scrapper.perform_scrapping()
        to_edit = self.model.objects.get(id=self.object.id)
        to_edit.pret_altex = scrapper.get_pret_altex()
        to_edit.pret_emag = scrapper.get_pret_emag()
        to_edit.descriere = scrapper.get_descriere_altex()
        to_edit.imagine = scrapper.get_imagine()
        to_edit.url_altex = scrapper.get_url_altex()
        to_edit.url_emag = scrapper.get_url_emag()
        to_edit.save()
        print(scrapper)
        return reverse("scraper:results_view")


class ResultView(LoginRequiredMixin, ListView):
    model = Produse
    template_name = 'altex_vs_emag/cautare_index.html'
    fields = ['cod_produs', 'descriere', 'pret_emag', 'pret_altex', 'imagine', 'url_altex']
    paginate_by = 5
    queryset = model.objects.filter(active=1)
    context_object_name = 'scraper'

    def get_context_data(self, *args, **kwargs):
        data = super(ResultView, self).get_context_data(*args, **kwargs)
        data['scraper'] = self.model.objects.filter(active=1)
        return data


class UpdateProductView(LoginRequiredMixin,UpdateView):
    model = Produse
    template_name = 'altex_vs_emag/results_view.html'
    fields = ['cod_produs']

    def get_success_url(self):
        return reverse('scraper:results_view')

@login_required
def delete_product(request, pk):
    Produse.objects.filter(id=pk).update(active=0)
    return redirect('scraper:results_view')


@login_required
def activate_product(request, pk):
    Produse.objects.filter(id=pk).update(active=1)
    return redirect('scraper:results_view')


class ProductInactiveView(ListView):

    model = Produse
    template_name = 'altex_vs_emag/cautare_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=0)
    context_object_name = 'scraper'

    def get_context_data(self, *args, **kwargs):
        data = super(ProductInactiveView, self).get_context_data(*args, **kwargs)
        data['scraper'] = self.model.objects.filter(active=0)
        return data
