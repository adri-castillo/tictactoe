from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default=' ' * 9) 
    turn=models.CharField(max_length=1, default='O')
    winner = models.CharField(max_length=1, null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Game {self.id} - Turn: {self.turn}'