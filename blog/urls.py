"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.views.generic import RedirectView
from django.views.static import serve
#from accounts.views import about,logout, login, registration, user_profile
from accounts.views import about
from accounts import urls as accounts_urls

from products import urls as urls_products

from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from products.views import all_products, products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='about'),
    url(r'^$', about, name="about"),
    url(r'^$', products, name="products"),
    
#     url(r'^$', index, name="index"),

    url(r'^accounts/', include(accounts_urls)),
   
#    url(r'^accounts/logout/$', logout, name="logout"),
#    url(r'^accounts/login/$', login, name="login"),
#    url(r'^accounts/register/$', registration, name="registration"),
#    url(r'^accounts/profile/$', user_profile, name="profile"),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
  
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
     url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})   
#    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
  
]
