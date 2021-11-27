import json
from django.db.models.expressions import F
from numpy.core import records
import pandas as pd
import traceback

from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import render
from django.http import HttpResponse

from search.models import MedicineModel

def home(request):
    return render(request,'home.html')

@action(detail=True)
def search_by_name(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            result_set = pd.DataFrame(MedicineModel.objects.filter(
                sku_name__icontains=name).values())
            result_set.drop('id',axis=1,inplace=True)
            result = result_set.to_html(index=False)
            context = {'name':name,'data':result}
            return render(request,'results.html',context)
    except Exception as exception:
        return HttpResponse("No Data Available", status=status.HTTP_404_NOT_FOUND)


@action(detail=True)
def search_by_manufacturer(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('manufacturer')
            result_set = pd.DataFrame(MedicineModel.objects.filter(
                manufacturer_name__icontains=name).values())
            result_set.drop('id',axis=1,inplace=True)
            result = result_set.to_html(index=False)
            context = {'name':name,'data':result}
            return render(request,'results.html',context)
    except Exception as exception:
        return HttpResponse("No Data Available", status=status.HTTP_404_NOT_FOUND)

@action(detail=True)
def search_by_salt(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('salt')
            result_set = pd.DataFrame(MedicineModel.objects.filter(
                salt_name__icontains=name).values())
            result_set.drop('id',axis=1,inplace=True)
            result = result_set.to_html(index=False)
            context = {'name':name,'data':result}
            return render(request,'results.html',context)
    except Exception as exception:
        return HttpResponse("No Data Available", status=status.HTTP_404_NOT_FOUND)
