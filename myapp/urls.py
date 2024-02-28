from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:type_no>/', views.detail, name='detail'),
    path('sum/<int:type_no>/', views.sum, name='sum'),
    path('dateT/<int:year>/<int:month>/', views.dateT, name='dateT'),
    path('display/', views.display, name='display'),
    ]

