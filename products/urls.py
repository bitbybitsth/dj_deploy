from django.urls import path
from products.views import *

urlpatterns = [
    path('all/', all_data),
    path('one/<int:id>',get_one),
    path('filter',filter_recs),
    path('exclude',exclude_data),
path('order',order_data),
path('look',look_up),
path('check',manager_demo)

]