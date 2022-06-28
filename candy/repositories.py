from .models import Candy


class CandyRepository:

    @staticmethod
    def get_all_candy(limit: int = 0) -> Candy:
        candies = Candy.objects.all()
        if limit:
            return candies[:limit]
        return candies

    @staticmethod
    def filter_candy(limit: int = 0, name: str = '') -> Candy:
        if name:
            candies = Candy.objects.filter(name__contains=name)
            if limit == 1:
                return candies.first()
            if limit:
                return candies[:limit]
            return candies
