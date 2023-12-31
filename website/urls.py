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


    path('products', views.products, name='products'),
    path('product/<int:pk>/', views.product_record, name='product_record'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/update/<int:pk>/', views.update_product, name='update_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),



    path('leads', views.leads, name='leads'),
    path('leads/<int:pk>/', views.lead_record, name='lead_record'),
    path('leads/add/', views.add_lead, name='add_lead'),
    path('leads/update/<int:pk>/', views.update_lead, name='update_lead'),
    path('leads/delete/<int:pk>/', views.delete_lead, name='delete_lead'),



    # Reports
    path('sales_report/managers/', views.sales_report_by_managers,
         name='sales_report_by_managers'),
    path('sales_report_by/products/', views.sales_report_by_products,
         name='sales_report_by_products'),


    # Charts
    path('sales_report/chart/', views.sales_report_chart,
         name='sales_report_chart'),


    path('products', views.products, name='products'),
    path('product/<int:pk>/', views.product_record, name='product_record'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/update/<int:pk>/', views.update_product, name='update_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),



    path('product_orders/', views.product_orders, name='product_orders'),
    path('product_order/<int:pk>/', views.product_order_record,
         name='product_order_record'),
    path('product_order/delete/<int:pk>/',
         views.delete_product_order, name='delete_product_order'),
    path('product_order/add/', views.add_product_order, name='add_product_order'),
    path('product_order/update/<int:pk>/',
         views.update_product_order, name='update_product_order'),


]
