from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User

"""
This SignUpForm, is a custom user registration form that extends Django's UserCreationForm. 

1. It adds an email field, making it a required field for registration.
2. The Meta class specifies that this form is for the User model and includes the username, email, password1, and password2 fields.
3. The clean_email method checks if the email already exists in the database, raising a validation error if it does.
4. The save method saves the user instance, ensuring the email is saved to the user model.
"""

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user