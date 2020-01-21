from django.shortcuts import render, redirect 
from django.core.urlresolvers import reverse
from .forms import ReviewForm
from .models import Product

# Create your views here.
def products(request):
 
    return render(request, "products.html")





def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def products_details(request, pk):
    product= Product.objects.get(id=pk)
    review_form=ReviewForm()
    return render(request, "products_details.html", {"product": product, "review_form": review_form})
    
#def add_review(request):
#    if request.method == "POST":
#        review_form = ReviewForm(request.POST)
#        if review_form.is_valid():
#            review_form.save()
#        return redirect(reverse("products"))

#this code is to be review
def add_review(request, pk):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            product = Product.objects.create(reviews=review_form.save())
    return redirect(reverse('products'))

