from django.contrib import admin
from .models import Contacts, OrderStatus, Contacts, Companies, Managers, Orders, OrderStatus, Leads, JobPosition, Department, Product, LeadStatus


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "company",
                    "job_title", "phone", "email", "description", "created_at")
    search_fields = ("first_name", "last_name", "company",
                     "job_title", "phone", "email", "description", "created_at")
    list_per_page = 10


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "city", "state", "zipcode",
                    "industry", "website", "year_founded", "number_of_employees", "manager")
    search_fields = ("name", "phone", "email", "city", "state", "zipcode", "industry", "website",
                     "year_founded", "number_of_employees", "manager__first_name", "manager__last_name")
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "price_per_unit",
                    "minimum_stock_level")
    search_fields = ("name",)
    list_per_page = 10


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    list_per_page = 10


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("order_status", "order_id", "company", "product", "quantity",
                    "shipping_date", "shipping_address", "order_amount", "manager", "created_at")
    search_fields = ("order_id", "company__name", "product__name",
                     "manager__first_name", "manager__last_name")
    list_per_page = 10


@admin.register(Managers)
class ManagersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone",
                    "email", "job_title", "department")
    search_fields = ("first_name", "last_name", "phone",
                     "email", "job_title__name", "department__name")
    list_per_page = 10


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_per_page = 10


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 10


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email",
                    "creation_date", "lead_status", "lead_source", "expected_close_date")
    search_fields = ("first_name", "last_name", "phone",
                     "email", "lead_status", "lead_source")
    list_per_page = 10


@admin.register(LeadStatus)
class LeadStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 10
