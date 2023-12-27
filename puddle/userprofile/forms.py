from django import forms
from userprofile.models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['username','email','password1','password2']
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Please repeat the password', 'class': 'w-full py-4 px-6 rounded-xl'}))

def form_validation_error(form):
    """
    Form Validation Error
    If any error happened in your form, this function returns the error message.
    """
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg
