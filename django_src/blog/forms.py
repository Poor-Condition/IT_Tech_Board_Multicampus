from django import forms
from .models import User, Jobs, Study

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['성별', 'email', '휴대폰번호', '관심사1', '관심사2']


class CreateStudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['name', 'location', 'time', 'max_member']


# class StudyMemberChange(forms.ModelForm):
#     def member_change(self):
#         if "signup" in self.data:
#             if self.members.count() >= max_member:
#                 raise Exception("해당 스터디는 정원을 초과했습니다.")
#             else:
#                 self.members.add(user)
#         elif "cancel" in self.data:
#             self.members.remove(user)

#     class Meta:
#         model = Study
#         fields = ['members', 'max_member']
