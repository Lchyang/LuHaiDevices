from django import forms


class AccountForm(forms.Form):
    username = forms.CharField(max_length=30, verbose_name='用户名')
    password = forms.CharField(max_length=64, verbose_name='密码')
    email = forms.EmailField(verboase_name='邮箱')
    tell = forms.IntegerField(blank=False, verbose_name='手机号',)