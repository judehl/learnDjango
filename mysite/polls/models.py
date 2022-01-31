import datetime
from django.utils import timezone

from django.db import models


# Create your models here.

class Question(models.Model):
    """
    问题列表
    """
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('时间')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        给模型增加特殊标签
        """
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    问题选项列表
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text
