from .repositories import CartItemRepository
from .utils import CartSessionManager
from .models import CartItem


class CartService:
    __slots__ = (
        'request',
        'session_manager',
    )

    def __init__(self, request):
        self.session_manager = CartSessionManager(request)

    def _get_session_cart_items(self):
        return self.session_manager.get_session_cart()

    @staticmethod
    def _build_context(cart_items) -> dict:
        return {
            'title': 'Корзина',
            'cart_items': cart_items
        }

    def execute(self):
        cart_items = CartItem.objects.filter(pk__in=[self._get_session_cart_items()])
        return self._build_context(cart_items)
