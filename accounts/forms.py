from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

INPUT = (
    "w-full rounded-lg border border-line bg-white/60 px-4 py-2.5 text-sm "
    "text-ink placeholder:text-muted focus:outline-none focus:ring-2 focus:ring-navy/40"
)
PASSWORD_INPUT = INPUT + " pr-11"


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": INPUT})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": INPUT})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": INPUT})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": PASSWORD_INPUT})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", "class": PASSWORD_INPUT})
    )
    terms = forms.BooleanField(
        error_messages={"required": "You must agree to the terms to continue."}
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_password1(self):
        password = self.cleaned_data["password1"]

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must include a number.")
        if password.isalnum():
            raise forms.ValidationError("Password must include a symbol.")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords don't match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email                   
        user.set_password(self.cleaned_data["password1"]) 
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": INPUT, "autofocus": True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": PASSWORD_INPUT})
    )

    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "Incorrect email or password.",
    }

    def clean_username(self):
        return self.cleaned_data["username"].lower()