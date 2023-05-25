from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from core.product.models import Product
from core.product.forms import ProductForm

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class ProductListView(ListView):
    model = Product
    template_name = "list_product.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('add_product')
        context['list_url'] = reverse_lazy('list_product')
        context['entity'] = 'Productos'
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "create.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('list_product')
        context['action'] = 'add'
        return context
    
    def get_success_url(self):
        return reverse("list_product")
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('list_product')
        context['action'] = 'edit'
        return context
    
    def get_success_url(self):
        return reverse("list_product")



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('list_product')
        return context
    
    def get_success_url(self):
        return reverse("list_product")

