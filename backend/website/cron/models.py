from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class c(models.Model):
    flag = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.flag}"

class Review_scheduling(models.Model):
    created_at = models.DateTimeField()

    def is_15_days_old(self):
        return now() >= self.created_at + timedelta(days=15)
    
    def __str__(self):
        return f"{self.created_at}"
