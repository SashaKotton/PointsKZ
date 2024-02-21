from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from products.forms import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.all(), pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def add_new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = form.instance
            return redirect('product_detail', pk=product.pk)
        pass
    else:
        form = ProductForm()
    return render(request, 'products/add_new_product.html', {'form': form })

def edit_product(request, pk):
    product = get_object_or_404(Product.objects.all(), pk = pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            product = form.instance
            return redirect('product_detail', pk=product.pk)
        pass
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/add_new_product.html', {'form': form, 'product': product })