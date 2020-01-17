#this code is to be review
from django.conf.urls import url, include
from .views import all_products, products_details, add_review

urlpatterns = [
    
    
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', products_details, name="details"),
    url(r'^(?P<pk>\d+)/add_review$', products_details, name='product_detail'),

    url(r'^add_review$', add_review, name="add_review"),
]