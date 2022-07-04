from .models import CartItem


class CartItemRepository:

    @staticmethod
    def get_all_cart_items(limit: int = 0) -> CartItem:
        cart_items = CartItem.objects.all()
        if limit:
            return cart_items[:limit]
        return limit



