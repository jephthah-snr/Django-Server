from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from crispy_forms.layout import Field
from django.utils.translation import gettext_lazy as _


class userregister(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email', 'password1', 'password2',]
        help_texts = {
            'username':None,
            'email':None,
            'password':None
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('Username')}),
            'email': forms.EmailInput(attrs={'placeholder': _('example@email.com')}),
            'password1': forms.PasswordInput(attrs={'placeholder': _('password')}),
            'password2': forms.PasswordInput(attrs={'placeholder': _('password2')}),
        }
    def __init__(self, *args, **kwargs):
        super(userregister, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': (_("Password"))})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': (_("Confirm password"))})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': (_("example@email.com"))})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': (_("First name"))})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': (_("Last name"))})
        
class login_form(AuthenticationForm):
    class Meta():
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('Username or email')}),
            'password': forms.PasswordInput(attrs={'placeholder': _('Password')}),
        }
    def __init__(self, *args, **kwargs):
        super(login_form, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': (_("Password"))})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': (_("Username or Email"))})
        self.fields['password'].widget.attrs['class'] = 'uk-input uk-border-rounded'
        self.fields['username'].widget.attrs['class'] = 'uk-input uk-border-rounded'
        


class userupdateform(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

# class profileupdateform(forms.ModelForm):
    
#     class Meta:
#         model = profile
#         fields = [
#         'bio',
#         'category',
#         'profession',
#         'current_location',
#         'facebook_user', 
#         'twitter_user', 
#         'github' ,
#         'primary_education',
#         'secondary_education',
#         'tertiary_education',]

# class upload_resume(forms.ModelForm):
    
#     class Meta:
#         model = profile
#         fields = [
#         'resume', 'where_you_work_currently_work',
#     'tell_us_why_you_love_your_job']

#class change_profilepic(forms.ModelForm):
    
    #class Meta:
        #model = profile
        #fields = ['profile_pic']






