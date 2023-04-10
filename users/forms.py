from django import forms


class UsersForm(forms.Form):
    username = forms.CharField(label='username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class addUserForm(forms.Form):
    username = forms.CharField(label='username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email", max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
