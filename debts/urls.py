from django.urls import path
from debts.views import CalculateDebt, DebtsList


app_name = "debts"

urlpatterns = [
    path('calculate/', CalculateDebt.as_view(), name='calculate') ,
    path('list/', DebtsList.as_view(), name='list'),
]