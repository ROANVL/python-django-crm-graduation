# Generated by Django 4.2.5 on 2023-09-20 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('industry', models.CharField(default='', max_length=100)),
                ('website', models.URLField(blank=True, max_length=255, null=True)),
                ('year_founded', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('number_of_employees', models.PositiveIntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Job Positions',
            },
        ),
        migrations.CreateModel(
            name='LeadStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.department')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.jobposition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_stock_level', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=None)),
                ('shipping_date', models.DateField(verbose_name='Shipping Date')),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('order_description', models.TextField(blank=True, null=True)),
                ('order_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.companies')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.managers')),
                ('order_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.orderstatus')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lead_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=None)),
                ('lead_source', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('lead_description', models.TextField(blank=True, default=None, null=True)),
                ('expected_close_date', models.DateField(default=None)),
                ('lead_status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.leadstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.companies')),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='manager',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.managers'),
        ),
    ]
