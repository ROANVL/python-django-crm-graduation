from django.contrib import admin
from .models import Contacts, OrderStatus, Contacts, Companies, Managers, Orders, OrderStatus, Leads, JobPosition, Department, Product


class ContactsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "company",
                    "job_title", "phone", "email", "description", "created_at"]
    search_fields = ["first_name", "last_name", "company",
                     "job_title", "phone", "email", "description", "created_at"]
    list_per_page = 10


admin.site.register(Contacts)


admin.site.register(Companies)


admin.site.register(Product)
admin.site.register(OrderStatus)
admin.site.register(Orders)


admin.site.register(Managers)
admin.site.register(JobPosition)
admin.site.register(Department)

admin.site.register(Leads)
