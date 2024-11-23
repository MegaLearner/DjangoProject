from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Post


from .models import DoctorBook
from django.forms.models import inlineformset_factory

class DoctorBookForm(forms.ModelForm):
    class Meta:
        model = DoctorBook
        fields = ['doctor','civil_id','date_from', 'date_to']



















# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]
#
# class LoginForm (forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs = {'class': form-control}))
#     email = forms.CharField(widget=forms.TextdInput(attrs = {'class': form-control}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': form-control}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': form-control}))
#
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=65)
#     password = forms.CharField(max_length=65, widget=forms.PasswordInput)
#
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['username','email','password1','password2']
#
#
#
#
# #
# # class PostForm(forms.ModelForm):
# #     class Meta:
# #         model = Post
# #         fields = ["title", "description"]





