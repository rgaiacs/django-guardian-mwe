from django.db import models


class Question(models.Model):
    class Meta:
        permissions = (("answer", "Answer"),)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class QuestionWithText(Question):
    answer = models.TextField()


class QuestionWithDuration(Question):
    answer = models.DurationField()
