from django.shortcuts import render
from django.views import generic
from .models import Paginas
from django.urls import reverse, reverse_lazy
from .forms import PaginaForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

def home(request):
    return render(request, "home.html")

class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.   
class PaginaListView(generic.ListView):
    model = Paginas
    template_name = "lista.html"

class PaginaDetailView(generic.DetailView):
    model = Paginas
    template_name = "detalle.html"

@method_decorator(staff_member_required, name='dispatch')
class PaginaCreateView(generic.CreateView):
    model = Paginas
    form_class = PaginaForm
    template_name = "nuevo.html"
    success_url = reverse_lazy('pags:lista')

@method_decorator(staff_member_required, name='dispatch')
class PaginaUpdateView(generic.UpdateView):
    model = Paginas
    form_class = PaginaForm
    template_name = "editar.html"

    def get_success_url(self):
        return reverse_lazy('pags:editar', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PaginaDeleteView(generic.DeleteView):
    model = Paginas
    template_name = "borrar.html"
    success_url = reverse_lazy('pags:lista')

