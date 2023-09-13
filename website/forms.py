from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contacts, Companies, Managers, Orders, OrderStatus, Leads, JobPosition, Department


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    # New field for agreement checkbox
    agree_to_terms = forms.BooleanField(
        label="I agree to the terms and conditions", required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2", "agree_to_terms")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# Create add record form


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = [
            "first_name",
            "last_name",
            "job_title",
            "phone",
            "email",
            "company",
            "description",
            "date_of_birth",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "job_title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Job Title"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "company": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "placeholder": "2020-01-02"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Заполните поле 'company' данными из модели Companies
        self.fields['company'].queryset = Companies.objects.all()


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = [
            "name",
            "phone",
            "email",
            "address",
            "city",
            "state",
            "zipcode",
            "industry",
            "website",
            "year_founded",
            "number_of_employees",
            "manager",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Company Name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "State"}),
            "zipcode": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zipcode"}),
            "industry": forms.TextInput(attrs={"class": "form-control", "placeholder": "Industry"}),
            "website": forms.URLInput(attrs={"class": "form-control", "placeholder": "Website"}),
            "year_founded": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Year Founded"}),
            "number_of_employees": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of Employees"}),
            "manager": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Заполните поле 'manager' данными из модели Managers
        self.fields['manager'].queryset = Managers.objects.all()


class AddManagerForm(forms.ModelForm):
    class Meta:
        model = Managers
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "job_title",
            "department",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            # Используем виджет Select
            "job_title": forms.Select(attrs={"class": "form-control"}),
            # Используем виджет Select
            "department": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Получаем список доступных должностей и отделов из базы данных
        job_positions = JobPosition.objects.all()
        departments = Department.objects.all()

        # Создаем выборки для полей job_title и department
        self.fields['job_title'].queryset = job_positions
        self.fields['department'].queryset = departments


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            "order_date",
            "order_amount",
            "company",
            "manager",
            "order_status",
            "order_description",
            "shipping_address",
        ]
        widgets = {
            "order_date": forms.DateInput(attrs={"class": "form-control", "placeholder": "Order Date"}),
            "order_amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Order Amount"}),
            "company": forms.Select(attrs={"class": "form-control", "placeholder": "Company"}),
            "manager": forms.Select(attrs={"class": "form-control", "placeholder": "Manager"}),
            # Используем виджет Select
            "order_status": forms.Select(attrs={"class": "form-control"}),
            "order_description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Order Description"}),
            "shipping_address": forms.Textarea(attrs={"class": "form-control", "placeholder": "Shipping Address"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Получаем список доступных статусов заказа из базы данных
        order_statuses = OrderStatus.objects.all()

        # Создаем выборку для поля order_status
        self.fields['order_status'].queryset = order_statuses


class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "creation_date",
            "status",
            "lead_source",
            "lead_description",
            "expected_close_date",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "creation_date": forms.DateInput(attrs={"class": "form-control", "placeholder": "Creation Date"}),
            "status": forms.TextInput(attrs={"class": "form-control", "placeholder": "Status"}),
            "lead_source": forms.TextInput(attrs={"class": "form-control", "placeholder": "Lead Source"}),
            "lead_description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Lead Description"}),
            "expected_close_date": forms.DateInput(attrs={"class": "form-control", "placeholder": "Expected Close Date"}),
        }
