from django.views.generic import DetailView

from .services import CartService
from .models import CartItem


# Create your views here.


class CartView(DetailView):
    model = CartItem
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart_context = CartService(self.request).execute(self.object)
        return context | cart_context
