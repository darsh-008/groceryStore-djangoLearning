# from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from myapp.forms import *
# from myapp import urlpatterns
from django.urls import include

# # Create your views here.
# def landing(request):
#     urlList = []
#     for ur in include('myapp.urls'):
#         urlList.append(str(ur))
#
#     return render(request, 'myapp/landing.html', {'urlList': urlList})


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
# def orderStatus(request):
#     status = OrderItem.objects.filter(status=1).get()
#     status1 = OrderItem.objects.filter(status=2).get()
#     return render(request, 'myapp/orderstatus.html', {'status': status, 'status1':status1})


def about(request):
    clientlist = Client.objects.all()
    return render(request, 'myapp/about.html', context={'clientlist':clientlist})

def detail(request, type_no):
    selected_type = get_object_or_404(Type, pk=type_no)
    items = item.objects.filter(type=selected_type).order_by("-price")
    return render(request, 'myapp/detail.html', {'selected_type': selected_type, 'items': items, 'type_no':type_no})
    # response = HttpResponse()
    # heading1 = '<h2>' + 'Items for Type ' + str(type_no) + ': ' + '</h2>'
    # response.write(heading1)
    # for etem in items:
    #     para = '<p>' + str(etem.name)+ ' = ' + str(etem.price) + '</p>'
    #     response.write(para)
    #
    # return response

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


def display(request):
    age =  18
    name = "darsh"
    return render(request, 'myapp/display.html', context={'age': age, 'name':name})


def items(request):
    # itemlists = OrderItem.objects.all().order_by('id')[:20]
    itemlists = item.objects.all()
    return render(request, 'myapp/items.html', context={'itemlists':itemlists})

# def placeorder(request):
#     form = OrderItemForm()
#     return render(request, 'myapp/placeorder.html', context={'form':form})

def placeorder(request):
    msg = ''
    itemlist = item.objects.all()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.quantity_ordered <= order.item.stock:
                order.save()
                msg = 'Your order has been placed successfully.'
                # Update stock field of the corresponding item
                order.item.stock -= order.quantity_ordered
                order.item.save()
                return render(request, 'myapp/order_response.html', {'msg': msg})
            else:
                msg = 'We do not have sufficient stock to fill your order.'
                return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})


def itemsearch(request):
    selected_item = None
    price = None

    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            selected_item_id = form.cleaned_data['items']
            selected_item = item.objects.get(pk=selected_item_id.id)
            price = selected_item.price

    else:
        form = ItemSearchForm()

    return render(request, 'myapp/itemsearch.html', {'form': form, 'selected_item': selected_item, 'price':price})

def itemdetail(request, item_id):
    i = get_object_or_404(item, pk=item_id)
    name = item.objects.get(pk=item_id).name
    price = item.objects.get(pk=item_id).price
    inter = item.objects.get(pk=item_id).interested
    form = InterestForm
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interested = int(form.cleaned_data['interested'])
            i.interested += interested
            i.save()
        else:
            form = InterestForm()
    return render(request, 'myapp/itemdetail.html', {'i': i,'form':form, 'name':name, 'price':price, 'inter':inter })