from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .login_decorator import login_required
from .forms import SignUpForm, AddRecordForm, AddCompanyForm, AddManagerForm, AddOrderForm, AddLeadForm
from .models import Contacts, Managers, Companies, Orders, Leads


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
    form = AddOrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "The order has been successfully added.")
            return redirect("orders")
    return render(request, 'add_order.html', {"form": form})


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
