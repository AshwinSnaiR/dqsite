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


DATABASE_CHOICES = [
    ('redshift', 'Redshift'),
    ('postgresql', 'Postgresql'),
    ('sqlserver', 'SQLServer'),
]


class createDatabaseForm(forms.Form):
    databaseName = forms.CharField(label='Database Name', max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourceType = forms.CharField(label='Source Type',
                                 widget=forms.Select(choices=DATABASE_CHOICES, attrs={'class': 'form-control'}))
    database = forms.CharField(label='Database', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    schemaName = forms.CharField(label='Schema Name', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    hostName = forms.CharField(label='Host Name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='User Name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    port = forms.CharField(label='Port Number', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
