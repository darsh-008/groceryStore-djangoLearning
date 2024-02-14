# from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# # Create your views here.
def index(request):
    type_list = Type.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'type_list': type_list})


# def index(request):
#     item_list = item.objects.all().order_by('-price')[:10]
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types: ' + '</p>'
#     response.write(heading1)
#     for type in item_list:
#         para ='<p>'+ str(type.id) + ': ' + str(type) + '</p>'
#         response.write(para)
#
#     return response
def about(request):
    response = HttpResponse()
    heading1 = '<p>' + 'This is an Online Grocery Store ' + '</p>'
    response.write(heading1)
    return response

def detail(request, type_no):
    selected_type = get_object_or_404(Type, pk=type_no)
    items = item.objects.filter(type=selected_type).order_by("-price")
    response = HttpResponse()
    heading1 = '<h2>' + 'Items for Type ' + str(type_no) + ': ' + '</h2>'
    response.write(heading1)
    for etem in items:
        para = '<p>' + str(etem.name)+ ' = ' + str(etem.price) + '</p>'
        response.write(para)

    return response


def sum(request, type_no):
    selected_type = get_object_or_404(Type, pk=type_no)
    items = item.objects.filter(type=selected_type)
    response = HttpResponse()
    heading1 = '<h2>' + 'Sum of Items for Type ' + str(type_no) + ': ' + '</h2>'
    response.write(heading1)
    sum = 0
    for etem in items:
        sum += etem.price
        para = '<p>' + str(etem.name) + ': '+ str(etem.price)+'</p>'
        response.write(para)

    response.write("Sum =" + str(sum))

    return response

def dateT(request, year, month):
    response = HttpResponse()
    DaTe =datetime(month=month,year=year, day=1)
    para = '<h1>' + 'This is an Online Grocery Store -' + str(DaTe.strftime("%B %Y")) + '</h1>'
    response.write(para)
    return response
