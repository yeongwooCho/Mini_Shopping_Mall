from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.


def index(request):

    print(request.session.get('user'))

    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사 끝났을때 (로그인 되었을 때)
        self.request.session['user'] = form.email
        # form에 유저정보가 있었다.
        return super().form_valid(form)
        # super를 통해서 기존의 form valid함수를 호출한다.
