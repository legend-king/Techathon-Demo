from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.question}"
    
class Hint(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint = models.TextField()

    def __str__(self):
        return f"{self.hint}"