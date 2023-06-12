from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import Budget_table
from django.core import serializers

# Create your views here.

def Display_budget_app(request):
    
    date = datetime.datetime.now()
    
    Incomes = Budget_table.objects.filter(budget_type='inc')
    Expenses = Budget_table.objects.filter(budget_type='exp')
    
    total_income = sum([inc.income for inc in Incomes])
    total_expense = sum([exp.expense for exp in Expenses])
    
    
    try:
        expense_percentage = ( (total_expense / total_income) * 100 )   
    except :
        expense_percentage = 0
        
    context = {
        "date": date,
        "total_income": total_income,
        "remaining_income":( total_income - total_expense),
        "total_expense": total_expense,
        "Incomes": Incomes,
        "Expenses": Expenses,
        "expense_percentage": expense_percentage ,
    }
    
    return render(request, 'index.html', context)



def Add_budget(request):
    
    data = json.loads(request.body)
    
    if(data['Type'] == 'inc'):
        Budget_table.objects.create(
            budget_type=data['Type'],
            income=data['value'],
            description=data['description']
        )
    elif(data['Type'] == 'exp'):
        Budget_table.objects.create(
            budget_type=data['Type'],
            expense=data['value'],
            description=data['description']
        )
    
    return JsonResponse({"data": data }, safe = True)


def Delete_item(request, id):
    
    Budget_table.objects.filter(id=id).delete()
    
    return JsonResponse({"message": 'item deleted' }, safe = True)