from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from debts.models import Debts
from django.contrib import messages



class CalculateDebt(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'debts/calculate.html')
    
    def post(self, request):
        beginning = request.POST.get('beginning')
        ending = request.POST.get('ending')

        try:
            beg_date = datetime.strptime(beginning, '%Y-%m-%d')
            end_date = datetime.strptime(ending, '%Y-%m-%d')

            days = (end_date - beg_date).days

            if days < 0:
                messages.warning(request, "'To' date should be later than 'From' date")
                return redirect("debts:calculate")

            Debts.objects.create(
                bomdod=days, 
                peshin=days, 
                asr=days, 
                shom=days, 
                xufton=days, 
                user=request.user,
            )

            messages.success(request, "Successfully recorded you debts")

            return redirect("home")
        except:
            messages.warning(request, "Please enter both dates")

            return redirect("debts:calculate")