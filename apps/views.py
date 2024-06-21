from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

from apps.models import Product


# def nums_view(request):
#     result = ""
#     for i in range(1, 11):
#         result += f"{i}\n"
#     return HttpResponse(result)
#
#
# def order_list_view(request):
#     return TemplateResponse(request, 'apps/order_list.html')
#
#
# def advisors_list_view(request):
#     return TemplateResponse(request, 'apps/advisors_list.html')

def product_list_view(request):
    context = {
        "products": Product.objects.all()
    }
    return TemplateResponse(request, 'apps/product-list.html', context=context)


def order_list_view(request):
    context = {
        "products": Product.objects.all()
    }
    return TemplateResponse(request, 'apps/order-list.html', context=context)
