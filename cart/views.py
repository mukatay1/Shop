from django.views import View
from django.views.generic import TemplateView

from .services import CartService
from .models import CartItem
from .constants import CART_ID


# Create your views here.


class CartView(TemplateView):
    model = CartItem
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart_context = CartService(self.request).execute()
        return context | cart_context


class AddCartItemView(View):
    def post(self, request):
        if CART_ID in request.session:
            self.request.session[CART_ID].append(self.kwargs.get('pk'))
        else:
            self.request.session[CART_ID] = [self.kwargs.get('pk')]


class RemoveItemView(View):
    def post(self, request, *args, **kwargs):
        print(f'!!!!!!!!!!!!!!!{kwargs}')
        if CART_ID in request.session:
            self.request.session[CART_ID].remove(self.kwargs.get('pk'))
