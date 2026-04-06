from django.db import models


class Game(models.Model):
    board = models.CharField(max_length=9, default=" " * 9)
    turn = models.CharField(max_length=1, default="X")
    winner = models.CharField(max_length=10, null=True, blank=True)
    is_finished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Game {self.id} - Turn: {self.turn}"

    @property
    def duration(self):
        if not (self.finished_at and self.created_at):
            return "In progress"

        total_seconds = int((self.finished_at - self.created_at).total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        
        if minutes > 0:
            return f"{minutes} min {seconds} sec"
    
        return f"{seconds} seconds"


    @staticmethod
    def get_statistics():
        return {
            "total": Game.objects.filter(is_finished=True).count(),
            "wins_x": Game.objects.filter(winner="X").count(),
            "wins_o": Game.objects.filter(winner="O").count(),
            "draws": Game.objects.filter(winner="Draw").count(),
        }
