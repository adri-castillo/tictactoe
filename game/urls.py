from django.urls import path
from .views import GameListCreateAPIView, GameMoveAPIView, GameCancelAPIView

urlpatterns = [
    path("games/", GameListCreateAPIView.as_view(), name="game-list"),
    path(
        "games/<int:game_id>/move/<int:position>/",
        GameMoveAPIView.as_view(),
        name="game-move",
    ),
    path(
        "games/<int:game_id>/cancel/", GameCancelAPIView.as_view(), name="game-cancel"
    ),
]
