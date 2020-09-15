from django.shortcuts import render
from django.http import HttpResponse
import json
from first_app.models import UserInfo


# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")


def ret_json_data(request):
    return HttpResponse(json.dumps({"name": "Alice", "age": 50}), \
        content_type="application/json")


def inser_data(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    passwd = request.GET.get("password")
    UserInfo.objects.create(name=name, age=age, password=passwd)
    return HttpResponse("数据插入成功！")