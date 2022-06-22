from .constants import RECENT_VIEWS


class CandySessionManager:
    __slots__ = (
        'request',
    )

    def __init__(self, request):
        self.request = request

    def get_candy_session(self):
        return self.request.session.get(RECENT_VIEWS)

    def add_candy_session(self, candy_pk):
        self.request.session[RECENT_VIEWS].insert(0, candy_pk)

    def create_candy_session(self, candy_pk):
        self.request.session[RECENT_VIEWS] = [candy_pk]

    def remove_candy_session(self, candy_pk):
        self.request.session[RECENT_VIEWS].remove(candy_pk)

    def modifying_dictionary_in_session(self):
        self.request.session.modified = True
