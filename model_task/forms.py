from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, RateLimit
from django.utils import timezone
from django import forms

class SignupForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.set_password(self.cleaned_data["password"])
            instance.save()
            RateLimit.objects.create(user=instance, login_time=timezone.now, req_count=0)
        return instance
    

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "role",
            "password"
        ]

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    class Meta:
        fields = [
            "email",
            "password"
        ]