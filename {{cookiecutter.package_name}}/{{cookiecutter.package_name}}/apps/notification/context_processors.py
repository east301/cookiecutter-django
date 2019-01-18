#
#
#

from .models import Notification


def notification(request):
    return {
        'notifications': Notification.objects.filter(active=True)
    }
