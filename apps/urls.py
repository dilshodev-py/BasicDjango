from django.urls import path

from apps.views import product_list_view, order_list_view

# from apps.views import nums_view, order_list_view, advisors_list_view

urlpatterns = [
    # path("nums" , nums_view),
    # path("orders" , order_list_view),
    # path("advisors" , advisors_list_view),
    path('product-list' , product_list_view),
    path('order-list' , order_list_view)
]