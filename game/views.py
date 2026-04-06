from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer
from .logic import TicTacToeLogic
from django.utils import timezone

class GameListCreateAPIView(APIView):

    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        game = Game.objects.create()
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GameMoveAPIView(APIView):

    def post(self, request, game_id, position):
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(
                {"error": "Partida no encontrada"}, status=status.HTTP_404_NOT_FOUND
            )

        if game.is_finished:
            return Response(
                {"error": "Esta partida ya terminó"}, status=status.HTTP_400_BAD_REQUEST
            )

        success, message = TicTacToeLogic.make_move(game, position)

        if not success:
            return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = GameSerializer(game)
        return Response(serializer.data)


class GameCancelAPIView(APIView):
    def post(self, request, game_id):
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(
                {"error": "Partida no encontrada"}, status=status.HTTP_404_NOT_FOUN
            )

        if game.is_finished:
            return Response(
                {"error": "La partida ya está finalizada o cancelada"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        game.is_finished = True
        game.winner = "Canceled"
        game.finished_at = timezone.now()
        game.save()

        serializer = GameSerializer(game)

        return Response(
            {"message": "Partida cancelada con éxito", "game": serializer.data},
            status=status.HTTP_200_OK,
        )
