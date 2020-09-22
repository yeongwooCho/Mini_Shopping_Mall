from django import forms
from .models import Shopuser
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ObjectDoesNotExist


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):  # 검증!!!!
        # 얘는 이미 기본적으로 만들어 져있는 함수이기에 super를 통해서
        # 기존에 forms의 클래스 Form안의 clean 함수를 호출해주고
        cleaned_data = super().clean()
        # 만약 값이 들어있지 않았으면, 위의 코드에서 실패처리가 되어 나가게 된다.
        # 값이 다 들어왔다는 검증이 끝나면 아래의 코드를 실행한다.
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:  # 각 값들이 비어있지않고 들어있을때
            if password != re_password:  # 그 두 값이 다를 때
                self.add_error('password', '비밀번호가 서로 다릅니다')
                self.add_error('re_password', '비밀번호가 서로 다릅니다')
                # password field에 error message를 넣겠다
            else:  # 회원가입하는 코드
                shopuser = Shopuser(
                    email=email,
                    password=make_password(password)
                )
                shopuser.save()


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):  # 검증!!!!
        # 얘는 이미 기본적으로 만들어 져있는 함수이기에 super를 통해서
        # 기존에 forms의 클래스 Form안의 clean 함수를 호출해주고
        cleaned_data = super().clean()
        # 만약 값이 들어있지 않았으면, 위의 코드에서 실패처리가 되어 나가게 된다.
        # 값이 다 들어왔다는 검증이 끝나면 아래의 코드를 실행한다.
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                shopuser = Shopuser.objects.get(email=email)
            except ObjectDoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return
            if not check_password(password, shopuser.password):
                # check_password는 입력받은 password와 DB에 있는 incoding된 값을 서로 비교해준다.
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.email = shopuser.email
                # form안에 email속성 값을 만들어주고,
                # views.py에서 user로 form의 email을 전달해 줌으로써 화면에 이메일을 띄운다.
