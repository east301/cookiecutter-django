#
#
#

from django.db import models
from djchoices import ChoiceItem, DjangoChoices


class Notification(models.Model):
    class Levels(DjangoChoices):
        INFO = ChoiceItem('Info')
        SUCCESS = ChoiceItem('Success')
        WARNING = ChoiceItem('Warning')
        DANGER = ChoiceItem('Danger')

    id = models.AutoField(primary_key=True)

    order = models.IntegerField(default=1)
    level = models.CharField(max_length=255, choices=Levels.choices, default=Levels.INFO)
    message = models.CharField(max_length=255)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notifications'
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title
