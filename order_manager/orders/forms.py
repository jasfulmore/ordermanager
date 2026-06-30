from django import forms
from .models import Customer, Product, Order, OrderItem

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']
