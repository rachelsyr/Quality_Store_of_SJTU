from django.shortcuts import render,get_object_or_404
from .models import Discount
from .forms import DiscountForm
from shop.models import Shop,ShopType
# Create your views here.

def show_discount(request):
    context = {}
    context['shops'] = Shop.objects.all()
    context['shop_types'] =  ShopType.objects.all()
    context['discounts'] = Discount.objects.all()
    return render(request, 'dis_list.html',context)

def discount_type(request,shop_type_pk):
    context = {}
    shop_type = get_object_or_404(ShopType, pk=shop_type_pk)
    context['shops'] = Shop.objects.filter(shop_type=shop_type)
    context['shop_type'] = shop_type
    context['shop_types'] =  ShopType.objects.all()
    context['discounts']=Discount.objects.all()
    return render(request, 'discount_type.html', context)

def discount_detail(request,shop_pk):
    context = {}
    context['shop'] = get_object_or_404(Shop, pk=shop_pk)
    context['shop_types'] =  ShopType.objects.all()
    context['discounts'] = Discount.objects.all()

    new_discount = None

    if request.method == "SHOP":
        discount_form = DiscountForm(data=request.SHOP)
        if  discount_form.is_valid():
            # 通过表单直接创建新数据对象，但是不要保存到数据库中
            new_discount =  discount_form.save(commit=False)
            # 设置外键为当前文章
            new_discount.post = post
            # 将评论数据对象写入数据库
            new_discount.save()
    else:
        discount_form = DiscountForm()
    return render(request, 'dis_detail.html',context)