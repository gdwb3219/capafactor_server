from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import csv
import os


# Create your views here.

def index(request):
  return JsonResponse({"Hi": "안녕"})

def get_csv_data():
  csv_file_path = os.path.join(settings.BASE_DIR, 'factorapi', 'mockdata.csv')
  data = []
  try:
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        data.append(row)
  except FileNotFoundError:
    print(f"Error: CSV File not fount at {csv_file_path}")
  return data

def my_view(request):
  csv_data = get_csv_data()
  # csv_data를 활용하여 필요한 로직 처리
  return JsonResponse({'data': csv_data})