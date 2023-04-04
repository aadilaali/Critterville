from django.urls import path
from . import views
app_name='adminapp'
urlpatterns = [
    
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('category', views.category, name='category'),
    path('showusers/', views.showusers, name='showusers'),
    path('showpets/', views.showpets, name='showpets'),
    path('adminupdatebuyer/<int:id>', views.adminupdatebuyer, name='adminupdatebuyer'),
    path(' admindeleteuser/<int:id>', views. admindeleteuser, name=' admindeleteuser'),
    path('admin_updatepet/<int:id>', views.admin_updatepet, name='adminupdatepet'),
    path('admin_deletepet/<int:id>',views.admin_deletepet,name='admin_deletepet'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
]