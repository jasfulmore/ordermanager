from django.urls import path
from .views import HomeView, CustomerListView, CustomerDetailView, OrderListView, OrderDetailView, ProductListView, ProductDetailView, order_detail
from .views import customer_create



urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("customers/new/", customer_create, name="customer-create"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/<int:pk>/", order_detail, name="order-detail"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

]
