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
from core.product.views import *
from core.product.models import *

urlpatterns = [
     path('', ProductListView.as_view() , name='list_product'),
     path('add/', ProductCreateView.as_view() , name='add_product'),
     path('edit/<int:pk>/', ProductUpdateView.as_view() , name='edit_product'),
     path('delete/<int:pk>/', ProductDeleteView.as_view() , name='del_product'),
]