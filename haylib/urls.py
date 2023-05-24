"""
URL configuration for haylib project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import index, block, resens, roman, sobit, stix,search_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/block/',block , name='block'),
    path('products/resens/',resens , name='resens'),
    path('products/roman/',roman , name='roman'),
    path('products/sobit/',sobit , name='sobit'),
    path('products/stix/',stix , name='stix'),
    # path('products/search/', search_view, name='search'),
    path('search/', search_view, name='search')
    # path('search/', views.search, name='search'),
]

# if settings.DEBUG == True:
#     urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)