from django.db import models

class AbstractQuestion(models.Model):
    class Meta:
        abstract = True
        permissions = (("answer", "Answer"),)

class Question(AbstractQuestion):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class QuestionWithText(Question):
    answer = models.TextField()


class QuestionWithDuration(Question):
    answer = models.DurationField()
