from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


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


def contacts(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'contacts.html', {'records': records})
    else:
        messages.success(
            request, "To view that page, please log in.")
        return redirect('home')


def customers(request):
    if request.user.is_authenticated:
        return render(request, 'customers.html', {})
    else:
        messages.success(
            request, "To view that page, please log in.")
        return redirect('home')


def orders(request):
    if request.user.is_authenticated:
        return render(request, 'orders.html', {})
    else:
        messages.success(
            request, "To view that page, please log in.")
        return redirect('home')


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


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "To view that page, please log in.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "The record has been deleted successfully.")
        return redirect('contacts')
    else:
        messages.success(
            request, "To delete the record, you must be logged in.")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(
                    request, "The record has been successfully added.")
                return redirect("contacts")
        return render(request, 'add_record.html', {"form": form})
    else:
        messages.success(request, "To add a record, you must be logged in.")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(
                request, "The record has been successfully updated!")
            return redirect("contacts")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "To update a record, you must be logged in.")
        return redirect('home')
