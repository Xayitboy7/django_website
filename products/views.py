from ast import Index
from django.shortcuts import render
from products.models import Glav, Roman,Block, Stix, Sobit,  Resens
from .filters import GlavFilter
from django.db.models import Q
from .models import Glav
# from .models import Article

# Create your views here.
def index(request):
    context = {'title': 'HayLib', 'username': 'adminman',}
    return render(request,'products/index.html', context)

def block(request):
    context = {'title': 'Блоги',}
    return render(request,'products/block.html', context)

def resens(request):
    context = {'title': 'Рецензии',}
    return render(request,'products/resens.html', context)

def roman(request):
    context = {'title': 'Романы',}
    return render(request,'products/roman.html', context)

def sobit(request):
    context = {'title': 'События',}
    return render(request,'products/sobit.html', context)

def stix(request):
    context = {'title': 'Стихи',}
    return render(request,'products/stix.html', context)



# def search_view(request):
#     glav_filter = GlavFilter(request.GET, queryset=Glav.objects.all())    
#     filtered_glav = glav_filter.qs
#     query = request.GET.get('query')
#     Q(title__icontains=query)
#     Q(text__icontains=query)  # Поиск по тексту
#     blocks = Block.objects.filter(title__icontains=query)
#     indexes = Index.objects.filter(title__icontains=query)
#     resenses = Resens.objects.filter(title__icontains=query)
#     romans = Roman.objects.filter(title__icontains=query)
#     sobits = Sobit.objects.filter(title__icontains=query)
#     stixs = Stix.objects.filter(title__icontains=query)
#     results = list(blocks) + list(indexes) + list(resenses) + list(romans) + list(sobits) + list(stixs)
#     return render(request, 'products/search.html', {'glav_filter': glav_filter, 'filtered_stories': filtered_glav, 'results': results})
    # return render(request, 'products/search.html', {'results': results})


def block_view(request):
    query = request.GET.get('query')
    blocks = Block.objects.filter(title__icontains=query)
    return render(request, 'products/block.html', {'blocks': blocks})

# В представлении index_view
def index_search_view(request):
    query = request.GET.get('query')
    indexes = Index.objects.filter(title__icontains=query)
    return render(request, 'products/index.html', {'indexes': indexes})



def resens_view(request):
    query = request.GET.get('query')
    resenses = Resens.objects.filter(title__icontains=query)
    return render(request, 'products/resens.html', {'resenses': resenses})


def roman_view(request):
    query = request.GET.get('query')
    romans = Roman.objects.filter(title__icontains=query)
    return render(request, 'products/roman.html', {'romans': romans})


def sobit_view(request):
    query = request.GET.get('query')
    sobits = Sobit.objects.filter(title__icontains=query)
    return render(request, 'products/sobit.html', {'sobits': sobits})


def stix_view(request):
    query = request.GET.get('query')
    stixs = Stix.objects.filter(title__icontains=query)
    return render(request, 'products/stix.html', {'stixs': stixs})

def search_view(request):
    query = request.GET.get('query')
    
    glav_filter = GlavFilter(request.GET, queryset=Glav.objects.all())
    filtered_glav = glav_filter.qs
    
    results = (
        Block.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)) |
        Resens.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)) |
        Roman.objects.filter(Q(title__icontains=query) | Q(stix__icontains=query)) |
        Sobit.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)) |
        Stix.objects.filter(Q(title__icontains=query) | Q(stix__icontains=query))
    )
    
    return render(request, 'products/search.html', {'glav_filter': glav_filter, 'filtered_glav': filtered_glav, 'results': results})

