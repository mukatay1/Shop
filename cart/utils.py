from .constants import CART_ID


class CartSessionManager:
    __slots__ = (
        'request',
    )

    def __init__(self, request):
        self.request = request

    def get_session_cart(self):
        return self.request.session.get(CART_ID)

    def create_session_cart(self, candy_pk):
        self.request.session[CART_ID] = [candy_pk]

    def add_session_cart(self, candy_pk):
        self.request.session[CART_ID].append(candy_pk)

    def remove_session_cart(self, candy_pk):
        self.request.session[CART_ID].remove(candy_pk)

    def modifying_dictionary_in_session(self):
        self.request.session.modified = True
