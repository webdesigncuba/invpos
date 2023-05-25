from django.shortcuts import render
from django.views.generic import TemplateView
from core.client.models import Client
from core.sale.models import Sale
from core.product.models import Product
#from core.user.models import User

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'INVPOS'
        context['client'] = Client.objects.all().count()
        context['sale'] = Sale.objects.all().count()
        context['prod'] = Product.objects.filter(stock=0)
      #  context['user'] = User.objects.all().count()
        return context
