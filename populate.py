import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedicalNER.settings')

import django
django.setup()

from search.models import MedicineModel
from search.serializers import MedicineSerializer
import pandas as pd
import numpy as np

try:
    medicine_data = pd.read_csv('meddata.csv')
    medicine_data.replace(to_replace ="-",value = 0,inplace=True)
    medicine_data[['sku_id','product_id']]=medicine_data[['sku_id','product_id']].astype(float)
    medicine_data[['sku_id','product_id']]=medicine_data[['sku_id','product_id']].astype('int64')
    medicine_data.replace(to_replace =0,value = '-',inplace=True)
    medicine_dict = medicine_data.to_dict(orient='records')
    medicine_serializer = MedicineSerializer(data=medicine_dict,many=True)
    if medicine_serializer.is_valid(raise_exception=True):
        medicine_serializer.save()
        print("Medicine Data Loaded Successfully")
except Exception as exception:
    print(exception)