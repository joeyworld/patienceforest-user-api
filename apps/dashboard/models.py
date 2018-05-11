from django.db import models


class Dashboard(models.Model):
    nickname = models.CharField(max_length=20)
    score = models.PositiveIntegerField()
    stage = models.PositiveIntegerField()

    class Meta:
        db_table = '스코어보드'
        verbose_name = '인내의 숲 점수'
        verbose_name_plural = '인내의 숲 점수들'
