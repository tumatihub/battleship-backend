from django.db import models
from game.models import Players

class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=280)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+' - '+self.text

    class Meta:
        ordering = ['created']

