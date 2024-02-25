from django.urls import path
from pricingapp.views import PriceCreateView

app_name = "pricingapp"

urlpatterns = [
    path('create/', PriceCreateView.as_view(), name='create_price'),
]
