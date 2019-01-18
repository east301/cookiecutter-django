#
#
#

from django.contrib import admin
from django.contrib.auth.models import User

from . import models


admin.site.unregister(User)


@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    pass
