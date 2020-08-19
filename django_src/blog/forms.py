from django import forms
from .models import User, Jobs


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    re_password = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    #pw 암호화를 위해 meta가 아니라 따로 해줌
    class Meta:
        model = User
        fields = ['username', '이름', '성별', 'email','휴대폰번호', '관심사1', '관심사2']

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

        return cd['re_password']

