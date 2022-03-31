from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)
def product_list_view(request):
    all_objects = Product.objects.all()
    context = {
        'object_list': all_objects
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)  # This fetches object from DB

    if request.method == "POST":
        obj.delete()
        return redirect("../..")
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)

def product_detail_view(request, my_id):
    # obj = Product.objects.get(id=my_id)

    # Option 1 to return 404
    obj = get_object_or_404(Product, id=my_id) # This fetches object from DB

    # # Option 2 to return 404(using try/except)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'object': obj
    }
    return render(request, "products/product_dynamic_view.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # Re-render the form so that after saving data in backend DB it clears out the form
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, "products/product_detail.html", context)
