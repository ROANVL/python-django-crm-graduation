from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .login_decorator import login_required
from .forms import SignUpForm, AddRecordForm, AddCompanyForm, AddManagerForm, AddOrderForm, AddLeadForm, ProductForm
from .models import Contacts, Managers, Companies, Orders, Leads, Product
from django.db.models import Sum, F
from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
from django.db.models import Count


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Check if the user has agreed to terms
            if form.cleaned_data.get('agree_to_terms'):
                form.save()
                # Authenticate and login
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(
                    request, "Congratulations! Your registration was successful!")
                return redirect('home')
            else:
                messages.error(
                    request, "To register, you must agree to the terms and conditions.")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.success(
                request, "Incorrect login credentials. Please try again or register.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


@login_required
def contacts(request):
    records = Contacts.objects.all()
    return render(request, 'contacts.html', {'records': records})


@login_required
def products(request):
    products_records = Product.objects.all()
    return render(request, 'products.html', {'products_records': products_records})


@login_required
def companies(request):
    companies_records = Companies.objects.all()
    return render(request, 'companies.html', {'companies_records': companies_records})


@login_required
def managers(request):
    managers_records = Managers.objects.all()
    return render(request, 'managers.html', {'managers_records': managers_records})


@login_required
def orders(request):
    orders_records = Orders.objects.all()
    return render(request, 'orders.html', {'orders_records': orders_records})


@login_required
def leads(request):
    leads_records = Leads.objects.all()
    return render(request, 'leads.html', {'leads_records': leads_records})


@login_required
def contact_record(request, pk):
    contact_record = Contacts.objects.get(contact_id=pk)
    return render(request, 'contact_record.html', {'contact_record': contact_record})


@login_required
def product_record(request, pk):
    product_record = Product.objects.get(id=pk)
    return render(request, 'product_record.html', {'product_record': product_record})


@login_required
def company_record(request, pk):
    company_record = Companies.objects.get(company_id=pk)
    return render(request, 'company_record.html', {'company_record': company_record})


@login_required
def manager_record(request, pk):
    manager_record = Managers.objects.get(manager_id=pk)
    return render(request, 'manager_record.html', {'manager_record': manager_record})


@login_required
def order_record(request, pk):
    order_record = Orders.objects.get(order_id=pk)
    return render(request, 'order_record.html', {'order_record': order_record})


@login_required
def lead_record(request, pk):
    lead_record = Leads.objects.get(lead_id=pk)
    return render(request, 'lead_record.html', {'lead_record': lead_record})


@login_required
def delete_record(request, pk):
    delete_it = Contacts.objects.get(contact_id=pk)
    delete_it.delete()
    messages.success(request, "The record has been deleted successfully.")
    return redirect('contacts')


@login_required
def delete_product(request, pk):
    delete_it = Product.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "The record has been deleted successfully.")
    return redirect('products')


@login_required
def delete_company(request, pk):
    delete_it = Companies.objects.get(company_id=pk)
    delete_it.delete()
    messages.success(request, "The record has been deleted successfully.")
    return redirect('companies')


@login_required
def delete_manager(request, pk):
    delete_it = Managers.objects.get(manager_id=pk)
    delete_it.delete()
    messages.success(request, "The record has been deleted successfully.")
    return redirect('managers')


@login_required
def delete_order(request, pk):
    delete_it = Orders.objects.get(order_id=pk)
    delete_it.delete()
    messages.success(request, "The order has been deleted successfully.")
    return redirect('orders')


@login_required
def delete_lead(request, pk):
    delete_it = Leads.objects.get(lead_id=pk)
    delete_it.delete()
    messages.success(request, "The lead has been deleted successfully.")
    return redirect('leads')


@login_required
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully added.")
            return redirect("contacts")
    return render(request, 'add_record.html', {"form": form})


@login_required
def add_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully added.")
            return redirect("products")
    return render(request, 'add_product.html', {"form": form})


@login_required
def add_company(request):
    form = AddCompanyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully added.")
            return redirect("companies")
    return render(request, 'add_company.html', {"form": form})


@login_required
def add_manager(request):
    form = AddManagerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully added.")
            return redirect("managers")
    return render(request, 'add_manager.html', {"form": form})


@login_required
def add_order(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            # Проверка остатков продукции
            if order.product.quantity >= order.quantity:
                # Если есть достаточное количество товаров, вычитываем их и сохраняем заказ
                order.product.quantity -= order.quantity
                order.product.save()
                order.save()
                messages.success(
                    request, "The order has been successfully added.")
                # Перенаправление на страницу заказов
                return redirect('orders')
            else:
                # Если недостаточно товаров, выдаем сообщение
                if not messages.get_messages(request):
                    messages.error(
                        request, f"Unfortunately, we're out of stock at the moment. The current quantity of the product is: {order.product.quantity}")
        else:
            messages.error(
                request, 'Invalid form data. Please check your input.')

    else:
        form = AddOrderForm()  # Создание новой формы для заказа

    # Измененный запрос для сортировки заказов по убыванию order_id
    orders = Orders.objects.all().order_by('-order_id')

    return render(request, 'add_order.html', {"form": form, "orders": orders})


@login_required
def add_lead(request):
    form = AddLeadForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The lead has been successfully added.")
            return redirect("leads")
    return render(request, 'add_lead.html', {"form": form})


@login_required
def update_record(request, pk):
    current_record = Contacts.objects.get(contact_id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully updated!")
            return redirect("contacts")
    return render(request, "update_record.html", {"form": form})


@login_required
def update_product(request, pk):
    current_record = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=current_record)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully updated!")
            return redirect("products")
    return render(request, "update_product.html", {"form": form})


@login_required
def update_company(request, pk):
    current_record = Companies.objects.get(company_id=pk)
    form = AddCompanyForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(
            request, "The record has been successfully updated!")
        return redirect("companies")
    return render(request, "update_company.html", {"form": form})


@login_required
def update_manager(request, pk):
    current_manager = Managers.objects.get(manager_id=pk)
    form = AddManagerForm(request.POST or None, instance=current_manager)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully updated!")
            return redirect("managers")
    return render(request, "update_manager.html", {"form": form})


@login_required
def update_order(request, pk):
    current_record = Orders.objects.get(order_id=pk)
    form = AddOrderForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(
            request, "The order has been successfully updated!")
        return redirect("orders")
    return render(request, "update_order.html", {"form": form})


@login_required
def update_lead(request, pk):
    current_record = Leads.objects.get(lead_id=pk)
    form = AddLeadForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(
            request, "The lead has been successfully updated!")
        return redirect("leads")
    return render(request, "update_lead.html", {"form": form})


# REPORSTS
def sales_report(request):
    managers_sales = Managers.objects.annotate(
        total_sales=Sum('orders__order_amount'),
        job_title_name=F('job_title__title'),
        department_name=F('department__name')
    )

    sales_data = Orders.objects.values('product__name') \
        .annotate(total_sold=Sum('quantity'), total_sales=Sum('order_amount')) \
        .order_by('product__name')

    return render(request, 'sales_report.html', {'managers_sales': managers_sales, 'sales_data': sales_data})


def sales_report_by_managers(request):
    managers_sales = Managers.objects.annotate(
        total_sales=Sum('orders__order_amount'),
        job_title_name=F('job_title__title'),
        department_name=F('department__name')
    )

    return render(request, 'sales_report_by_managers.html', {'managers_sales': managers_sales, })


def sales_report_by_products(request):
    sales_data = Orders.objects.values('product__name') \
        .annotate(total_sold=Sum('quantity'), total_sales=Sum('order_amount')) \
        .order_by('product__name')

    return render(request, 'sales_report_by_products.html', {'sales_data': sales_data})


# CHARTS
def sales_report_chart(request):
    # Query the database to get total sales for each manager,
    # and annotate the results with job titles and department names.
    managers_sales = Managers.objects.annotate(
        total_sales=Sum('orders__order_amount'),
        job_title_name=F('job_title__title'),
        department_name=F('department__name')
    )

    # Extract the names of managers for labeling the x-axis.
    data_names = [
        f"{manager.first_name} {manager.last_name}" for manager in managers_sales]

    # Extract total sales values for each manager, filling with 0 if the value is missing.
    data_values = [
        manager.total_sales if manager.total_sales else 0 for manager in managers_sales]

    # Set the size and DPI (dots per inch) for the entire chart.
    plt.figure(figsize=(20, 8), dpi=80)

    # Create an Axes object to control the chart.
    ax = plt.subplot(111)

    # Create bars for the bar chart with specified color and width.
    bars = ax.bar(data_names, data_values, color='#06F', width=0.6)

    # Set the label and font style for the x-axis.
    plt.xlabel('Managers', fontstyle='italic', fontsize=16)

    # Set the label and font style for the y-axis.
    plt.ylabel('Total Sales', fontstyle='italic', fontsize=16)

    # Set the title and font style for the chart.
    plt.title('Sales Report by Managers', fontstyle='italic', fontsize=22)

    # Rotate x-axis labels for better readability.
    plt.xticks(rotation=45)

    # Add gridlines with blue dashed lines on the y-axis.
    ax.grid(True, axis='y', linestyle='--', alpha=0.7, color='blue')

    # Increase the font size of x-axis labels (managers).
    ax.set_xticklabels(data_names, fontsize=12)

    # Increase the font size of y-axis labels (total sales).
    ax.set_yticklabels(ax.get_yticks(), fontsize=12)

    # Ensure tight layout to avoid clipping labels.
    plt.tight_layout()

    # Create a buffer to save the chart as a PNG image.
    buffer = io.BytesIO()

    # Save the chart in PNG format with a transparent background.
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)

    # Clear the chart for reuse.
    plt.clf()

    # Create an HTTP response with the PNG image.
    response = HttpResponse(buffer.getvalue(), content_type='image/png')

    # Return the chart as an HTTP response.
    return response
