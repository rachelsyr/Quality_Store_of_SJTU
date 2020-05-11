from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop, ShopType
from django.contrib.postgres.search import SearchVector
from .forms import  SearchForm
from django.contrib.postgres.search import TrigramSimilarity

# Create your views here.
def shop_list(request):
    context = {}
    context['shops'] = Shop.objects.all()
    context['shop_types'] = ShopType.objects.all()
    return render(request, 'shop/shop_list.html', context)


def shop_detail(request, shop_pk):
     context = {}
     context['shop'] = get_object_or_404(Shop, pk=shop_pk)
     return render(request, 'shop/shop_detail.html', context)



def shop_with_type(request, shop_type_pk):
    context = {}
    shop_type = get_object_or_404(ShopType, pk=shop_type_pk)
    context['shops'] = Shop.objects.filter(shop_type=shop_type)
    context['shop_type'] = shop_type
    context['shop_types'] = ShopType.objects.all()
    return render(request, 'shop/shops_with_type.html', context)


#新增全文搜索功能，搜索范围是标题和简介
def shop_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            #search_vector = SearchVector('shop_name', 'detail')
            #目前只能完成根据精确匹配项计算出来的分数筛选出的项，
            #商店名的三元匹配已实现
            results= Shop.objects.annotate(
                                            similarity=TrigramSimilarity('name', query)*5+TrigramSimilarity('content', query),
                                            ).filter(similarity__gte=0.05).order_by('-similarity')
    context={   'query': query, 
                "form": form, 
                'results': results,
            }
    return render(request, 'shop/search.html', context
                                                      )