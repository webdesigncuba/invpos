# Copyright 2023 David Cordero Rosales
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path
from core.sale.views import *
from core.sale.models import *

urlpatterns = [
     path('', SaleListView.as_view() , name='list_sale'),
     path('add/', SaleCreateView.as_view() , name='add_sale'),
     path('edit/<int:pk>/', SaleUpdateView.as_view() , name='edit_sale'),
     path('delete/<int:pk>/', SaleDeleteView.as_view() , name='del_sale'),
      path('invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
]