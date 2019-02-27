from django.db import models

# Create your models here.

class Match(models.Model):
    match_num=models.IntegerField()
    round=models.TextField(blank=False)
    t1=models.TextField(blank=False)
    t1_score=models.IntegerField(default=0)
    t2=models.TextField(blank=False)
    t2_score=models.IntegerField(default=0)

    def __str__(self):
        return "Match " + str(self.match_num)
