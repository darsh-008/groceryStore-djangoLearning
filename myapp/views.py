# from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import *
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from myapp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# from myapp import urlpatterns
from django.urls import include, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# # Create your views here.
# def landing(request):
#     urlList = []
#     for ur in include('myapp.urls'):
#         urlList.append(str(ur))
#
#     return render(request, 'myapp/landing.html', {'urlList': urlList})


def index(request):
    # sessions
    if 'session_counter' in request.session:
        request.session['session_counter'] += 1
    else:
        request.session['session_counter'] = 1

    session_count = request.session['session_counter']

    # Get the current count from the cookie or set it to 0 if the cookie doesn't exist
    visit_count = int(request.COOKIES.get('visit_count', 0))

    # Increment the visit count
    visit_count += 1

    # Set the cookie with the updated visit count
    response = render(request, 'myapp/index.html', {'visit_count': visit_count, 'session_count': session_count})
    response.set_cookie('visit_count', visit_count, max_age=10)  # Set max age to 60 seconds

    return response


# class SignUpView(CreateView):
#     template_name = 'myapp/signup.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('index')  # Redirect to the index page after signup

# def get_success_url(self):
#     return reverse_lazy('login')  # Redirect to the login page after signup

def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('myapp:login')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    # logout(request)
    return redirect('myapp:logout_confirmation')

# def logout_confirmation(request):
#     return render(request, 'myapp/logout.html')

# @login_required
# def myorders(request):
#     if request.user.is_client:
#         orders = OrderItem.objects.filter(client=request.user)
#         return render(request, 'myapp/myorders.html', {'orders': orders})
#     else:
#         message = 'You are not a registered client!'
#         return render(request, 'myapp/myorders.html', {'message': message})

# @login_required
# def myorders(request):
# 	print("46-------", request.user.wrapped.dict_)
# 	try:
# 		email_address =  request.user.email
# 		client = Client.objects.get(email=email_address)
# 		print("49----",client)
# 		if request.user.user_typ == 'client':
# 			orders = OrderItem.objects.filter(client=request.user)
# 			return render(request, 'myapp/myorders.html', {'orders': orders})
# 		else:
# 		    message = 'You are not a registered client!'
# 		    return render(request, 'myapp/myorders.html', {'message': message})
# 	except Exception as e:
# 		print(e)
# 		message = 'You are not a registered client!'
# 		return render(request, 'myapp/myorders.html', {'message':message})
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
    # clientlist = Client.objects.all()
    form = CityForm()
    return render(request, 'myapp/about.html', context={'form': form})


def detail(request, type_no):
    selected_type = get_object_or_404(Type, pk=type_no)
    items = item.objects.filter(type=selected_type).order_by("-price")
    return render(request, 'myapp/detail.html', {'selected_type': selected_type, 'items': items, 'type_no': type_no})
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
        para = '<p>' + str(etem.name) + ': ' + str(etem.price) + '</p>'
        response.write(para)

    response.write("Sum =" + str(sum))

    return response


def dateT(request, year, month):
    response = HttpResponse()
    DaTe = datetime(month=month, year=year, day=1)
    para = '<h1>' + 'This is an Online Grocery Store -' + str(DaTe.strftime("%B %Y")) + '</h1>'
    response.write(para)
    return response


def display(request):
    age = 18
    name = "darsh"
    return render(request, 'myapp/display.html', context={'age': age, 'name': name})


def items(request):
    # itemlists = OrderItem.objects.all().order_by('id')[:20]
    itemlists = item.objects.all()
    return render(request, 'myapp/items.html', context={'itemlists': itemlists})


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

    return render(request, 'myapp/itemsearch.html', {'form': form, 'selected_item': selected_item, 'price': price})


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
    return render(request, 'myapp/itemdetail.html',
                  {'i': i, 'form': form, 'name': name, 'price': price, 'inter': inter})


def item_list(request):
    items = item.objects.all()
    price_range_form = PriceRangeForm(request.GET)

    if price_range_form.is_valid():
        min_price = price_range_form.cleaned_data.get('min_price')
        max_price = price_range_form.cleaned_data.get('max_price')
        if min_price is not None:
            items = items.filter(price__gte=min_price)
        if max_price is not None:
            items = items.filter(price__lte=max_price)

    return render(request, 'myapp/item_list.html', {'items': items, 'price_range_form': price_range_form})