from django.db import models
from decimal import Decimal
from django.utils import timezone


class JobPosition(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Job Positions"


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Departments"


class Managers(models.Model):
    manager_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField()
    job_title = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    industry = models.CharField(max_length=100, default='')
    website = models.URLField(max_length=255, null=True, blank=True)
    year_founded = models.PositiveIntegerField(
        null=True, blank=True, default=None)  # Дефолтное значение None
    number_of_employees = models.PositiveIntegerField(
        null=True, blank=True, default=None)  # Дефолтное значение None
    manager = models.ForeignKey(
        Managers, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100, default='')
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(
        null=True, blank=True, default=None)  # Дефолтное значение None
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class OrderStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_status = models.ForeignKey(
        OrderStatus, on_delete=models.SET_NULL, null=True, blank=True
    )
    order_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None, null=True)
    quantity = models.PositiveIntegerField(
        default=None)
    shipping_date = models.DateField(
        verbose_name="Shipping Date"
    )
    shipping_address = models.TextField(null=True, blank=True)
    order_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    manager = models.ForeignKey(
        Managers, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        if self.product and self.quantity is not None:
            self.order_amount = self.product.price_per_unit * self.quantity

        # Check if a company is associated with this order
        if self.company:
            # Build the shipping address from company data
            address_parts = []
            if self.company.address:
                address_parts.append(self.company.address)
            if self.company.city:
                address_parts.append(self.company.city)
            if self.company.state:
                address_parts.append(self.company.state)
            if self.company.zipcode:
                address_parts.append(self.company.zipcode)

            # Join address parts into a single string
            self.shipping_address = ", ".join(address_parts)

            # Set the manager from the associated company
            if self.company.manager:
                self.manager = self.company.manager

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.order_id}"


class Leads(models.Model):
    lead_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField()
    creation_date = models.DateField()
    status = models.CharField(max_length=50)
    lead_source = models.CharField(
        max_length=100, null=True, blank=True, default=None)  # Дефолтное значение None
    lead_description = models.TextField(null=True, blank=True)
    expected_close_date = models.DateField(
        null=True, blank=True, default=None)  # Дефолтное значение None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
