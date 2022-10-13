from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha de publicación')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now
    def add_geo_tag(self, geo_tag):
        self.geo_tag = geo_tag
        self.save()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicado recientemente?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
    geo_location = models.CharField(max_length=50)




    
