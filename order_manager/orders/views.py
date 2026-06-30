from django.views.generic import TemplateView, ListView, DetailView
from .models import Customer, Order, Product
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomerForm

# Create your views here.
def customer_create(request):
    form = CustomerForm(request.POST or None)
    # user submits form
    if request.method == "POST":
        form = CustomerForm(request.POST)

        # checks if data is valid
        if form.is_valid():
            form.save()
            return redirect("customer-create")
        

    return render(request, "customers/customer_form.html", {"form": form})

class HomeView(TemplateView):
    template_name = "home.html"


class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = 'customer'
    

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'product'


class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, "orders/order_detail.html", {
        "order": order
    })