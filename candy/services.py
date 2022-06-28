from .models import Candy
from .repositories import CandyRepository
from .utils import CandySessionManager
from .constants import RECENT_VIEWS


class CandyService:
    __slots__ = (
        'request',
    )

    def __init__(self, request):
        self.request = request

    def get_filtered_candies(self):
        input_data = self.request.GET.get('candy_search', 'Error')
        candies = CandyRepository.filter_candy(1, input_data)
        return candies

    @staticmethod
    def _build_context(candies):
        return {
            'candies': candies ,
            'title': 'Главная страница',
        }

    def execute(self):
        candies = CandyRepository.get_all_candy()
        return self._build_context(candies)


class CandyRecentService:
    __slots__ = (
        'request',
        'session_manager',
    )

    def __init__(self, request):
        self.request = request
        self.session_manager = CandySessionManager(request)

    def _get_candy_from_session(self):
        return self.session_manager.get_candy_session()

    def _create_candy_from_session(self, candy_pk):
        self.session_manager.create_candy_session(candy_pk)

    def _remove_candy_from_session(self, candy_pk):
        self.session_manager.remove_candy_session(candy_pk)

    def _add_candy_from_session(self, candy_pk):
        self.session_manager.add_candy_session(candy_pk)

    def _session_changing(self, candy_pk):
        if RECENT_VIEWS in self.request.session:
            if candy_pk in self._get_candy_from_session():
                self._remove_candy_from_session(candy_pk)
            self._add_candy_from_session(candy_pk)
        else:
            self._create_candy_from_session(candy_pk)
        self.session_manager.modifying_dictionary_in_session()
        if len(self._get_candy_from_session()) > 5:
            self.request.session[RECENT_VIEWS].pop()

    @staticmethod
    def _build_context(candies: list, name: str) -> dict:
        return {
            'candies': candies,
            'title': name,
        }

    def execute(self, candy_object):
        self._session_changing(candy_object.pk)
        candies = [Candy.objects.get(pk=i) for i in self._get_candy_from_session()]
        return self._build_context(candies, candy_object.name)
