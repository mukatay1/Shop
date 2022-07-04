from .repositories import CartItemRepository
from .utils import CartSessionManager
from .constants import CART_ID


class CartService:
    __slots__ = (
        'request',
        'session_manager',
    )

    def __init__(self, request):
        self.session_manager = CartSessionManager(request)

    def _get_session_cart_items(self):
        self.session_manager.get_session_cart()

    def _create_session_cart_items(self, cart_pk):
        self.session_manager.create_session_cart(cart_pk)

    def _execute_session_cart_items(self, candy_pk):
        if CART_ID in self.request.session:
            pass
        else:
            self._create_session_cart_items(candy_pk)

    @staticmethod
    def _build_context(cart_items) -> dict:
        return {
            'cart_items': cart_items
        }

    def execute(self, candy):
        self._execute_session_cart_items(candy.pk)
        cart_items = CartItemRepository.get_all_cart_items()
        return self._build_context(cart_items)
