from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),


    path('contacts', views.contacts, name='contacts'),
    path('contact_record/<int:pk>', views.contact_record, name='record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

    path('delete/<int:pk>', views.delete_record, name='delete_record'),


    path('companies', views.companies, name='companies'),
    path('company/<int:pk>/', views.company_record, name='company_record'),
    path('company/add/', views.add_company, name='add_company'),
    path('company/update/<int:pk>/',
         views.update_company, name='update_company'),
    path('company/delete/<int:pk>/',
         views.delete_company, name='delete_company'),


    path('managers', views.managers, name='managers'),
    path('managers/<int:pk>/', views.manager_record, name='manager_record'),
    path('managers/add/', views.add_manager, name='add_manager'),
    path('managers/update/<int:pk>/', views.update_manager, name='update_manager'),
    path('managers/delete/<int:pk>/', views.delete_manager, name='delete_manager'),

    path('orders', views.orders, name='orders'),
    path('orders/<int:pk>/', views.order_record, name='order_record'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/update/<int:pk>/', views.update_order, name='update_order'),
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),

    path('leads', views.leads, name='leads'),
    path('leads/<int:pk>/', views.lead_record, name='lead_record'),
    path('leads/add/', views.add_lead, name='add_lead'),
    path('leads/update/<int:pk>/', views.update_lead, name='update_lead'),
    path('leads/delete/<int:pk>/', views.delete_lead, name='delete_lead'),

    path('sales_report/managers/', views.sales_report_by_managers,
         name='sales_report_by_managers'),
    path('sales_report/chart/', views.sales_report_chart,
         name='sales_report_chart'),

]
