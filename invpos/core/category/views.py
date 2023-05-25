from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from core.category.models import Category
from core.category.forms import CategoryForm

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('add_category')
        context['list_url'] = reverse_lazy('list_category')
        context['entity'] = 'Categorias'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('list_category')
   # permission_required = 'erp.add_category'
    #url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('list_category')
        context['action'] = 'add'
        return context
    
    def get_success_url(self):
        return reverse("list_category")

    
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('list_category')
  #  permission_required = 'erp.change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('list_category')
        context['action'] = 'edit'
        return context

    def get_success_url(self):
        return reverse("list_category")



class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy('list_category')
   # permission_required = 'erp.delete_category'
    #url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        return context
    
    def get_success_url(self):
        return reverse("list_category")
