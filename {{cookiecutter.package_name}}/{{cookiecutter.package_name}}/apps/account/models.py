#
#
#

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        db_table = 'user_profiles'
