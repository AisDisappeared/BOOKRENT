from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'placeholder':'username','autofocus':'autofocus'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"placeholder":'password'}))

class OTPForm(forms.Form):
    otp = forms.CharField(label="OTP",max_length=6)


