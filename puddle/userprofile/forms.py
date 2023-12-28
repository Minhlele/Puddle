from django import forms
from userprofile.models import Profile

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'location', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name','class': 'w-full py-4 px-6 rounded-xl'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name','class': 'w-full py-4 px-6 rounded-xl'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Bio','class': 'w-full py-4 px-6 rounded-xl'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location','class': 'w-full py-4 px-6 rounded-xl'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone','class': 'w-full py-4 px-6 rounded-xl'}),
        }

    def save(self, user=None, commit=True):
        profile = super().save(commit=False)
        if user:
            profile.user = user
        if commit:
            profile.save()
        return profile
