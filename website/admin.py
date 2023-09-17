from django.contrib import admin
from .models import Contacts, OrderStatus, Contacts, Companies, Managers, Orders, OrderStatus, Leads, JobPosition, Department, Product


admin.site.register(Companies)
admin.site.register(Contacts)


admin.site.register(Product)
admin.site.register(OrderStatus)
admin.site.register(Orders)


admin.site.register(Managers)
admin.site.register(JobPosition)
admin.site.register(Department)

admin.site.register(Leads)
