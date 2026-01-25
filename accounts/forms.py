from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['cnic', 'full_name', 'constituency', 'password']

    def clean_cnic(self):
        cnic = self.cleaned_data['cnic']
        if not cnic.isdigit() or len(cnic) != 13:
            raise forms.ValidationError("CNIC must be exactly 13 digits")
        if User.objects.filter(cnic=cnic).exists():
            raise forms.ValidationError("CNIC already exists")
        return cnic
