from django.urls import path
from debts.views import CalculateDebt


app_name = "debts"

urlpatterns = [
    path('calculate/', CalculateDebt.as_view(), name='calculate')    
]