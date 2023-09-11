from django.db import models


class Managers(models.Model):
    manager_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Дефолтное значение пустой строки
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField()
    job_title = models.CharField(max_length=100, default='')
    department = models.CharField(
        max_length=100, null=True, blank=True, default=None)  # Дефолтное значение None
    start_date = models.DateField(
        null=True, blank=True, default=None)  # Дефолтное значение None

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
    social_media = models.URLField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(
        null=True, blank=True, default=None)  # Дефолтное значение None
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    manager = models.ForeignKey('Managers', on_delete=models.CASCADE)

    # Дефолтное значение пустой строки
    order_status = models.CharField(
        max_length=50, null=True, blank=True, default='')
    order_description = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.order_id}"


class Leads(models.Model):
    lead_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Дефолтное значение пустой строки
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
