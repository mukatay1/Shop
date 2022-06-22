from django.test import TestCase, RequestFactory

from .services import CandyRecentService
from .models import Candy
from .constants import RECENT_VIEWS


# Create your tests here.

class TestRecentCandy(TestCase):

    def setUp(self) -> None:
        self.candy1 = Candy.objects.create(
            name='Ананас',
            slug='Ananas',
        )
        self.candy2 = Candy.objects.create(
            name='Яблоко',
            slug='Apple',
        )
        self.candy3 = Candy.objects.create(
            name='Котлета',
            slug='Kotleta',
        )
        self.candy4 = Candy.objects.create(
            name='Жираф',
            slug='jeraf',
        )
        self.candy5 = Candy.objects.create(
            name='Капуста',
            slug='Kapusta',
        )
        self.candy6 = Candy.objects.create(
            name='Банан',
            slug='Banan',
        )

    def test_recent_candy(self):
        request = RequestFactory().get('')
        request.session = self.client.session
        CandyRecentService(request).execute(self.candy1)  # The first one will be deleted
        CandyRecentService(request).execute(self.candy3)
        CandyRecentService(request).execute(self.candy2)
        CandyRecentService(request).execute(self.candy4)
        CandyRecentService(request).execute(self.candy6)
        CandyRecentService(request).execute(self.candy5)
        self.assertEqual(request.session[RECENT_VIEWS], [5, 6, 4, 2, 3])  # Recent objects must be in that order
        self.assertEqual(len(request.session[RECENT_VIEWS]), 5)  # I need only five object
