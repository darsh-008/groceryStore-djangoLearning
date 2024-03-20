from django.urls import path
from . import views
from .views import *

app_name = 'myapp'
urlpatterns = [
    # path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('signup/', views.SignUpView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('about/', views.about, name='about'),
    path('<int:type_no>/', views.detail, name='detail'),
    path('sum/<int:type_no>/', views.sum, name='sum'),
    path('dateT/<int:year>/<int:month>/', views.dateT, name='dateT'),
    path('display/', views.display, name='display'),
    path('items/', views.items, name='items'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('itemsearch', views.itemsearch, name='itemsearch'),
    path('items/<int:item_id>/', views.itemdetail, name='itemdetail'),
    # path('myorders/', views.myorders, name='myorders'),
    path('itemList/', item_list, name='item_list'),
    ]

