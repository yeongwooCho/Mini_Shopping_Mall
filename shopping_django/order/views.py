from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm

from .models import Order
from django.views.generic import ListView

# Create your views here.


class OrderCreate(FormView):
    # 여기서 formview를 화면을 보여주는 용도로 쓰지 않기때문에
    # template_name는 필요없다.
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        # 기존에 있는 함수부터 호출해서 먼저 만들어 주고
        # 이제 kw라는 변수안에 기본적으로 이 FormView가 알아서 생성하는 인자값을 만들겠지
        # 그리고 거기다가 update를 하는 것이다.
        kw.update({
            'request': self.request
        })
        return kw
        # request라는 인자값을 추가해서 반환을 해주면
        # 기존에 자동으로 생성되는 인자값(kwargs)에다가
        # 'request'라는 인자겂도 함께 전달해서 Form class를 만들겠다


class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order_list'
