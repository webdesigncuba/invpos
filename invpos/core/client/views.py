from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.client.forms import ClientForm
#from core.erp.mixins import ValidatePermissionRequiredMixin
from core.client.models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
  #  permission_required = 'erp.view_client'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('add_client')
        context['list_url'] = reverse_lazy('list_client')
        context['entity'] = 'Clientes'
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'create.html'
    success_url = reverse_lazy('list_client')
  #  permission_required = 'erp.add_client'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('list_client')
        context['action'] = 'add'
        return context

    def get_success_url(self):
        return reverse("list_client")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'create.html'
    success_url = reverse_lazy('list_client')
   # permission_required = 'erp.change_client'
   # url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('list_client')
        context['action'] = 'edit'
        return context
    
    def get_success_url(self):
        return reverse("list_client")



class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'delete.html'
    success_url = reverse_lazy('list_client')
   # permission_required = 'erp.delete_client'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('list_client')
        return context

    def get_success_url(self):
        return reverse("list_client")



# Create your views here.
