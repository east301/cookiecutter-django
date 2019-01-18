#
#
#

from django.conf import settings


class WSGIScriptNameMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        script_name = request.META.get('SCRIPT_NAME')
        if script_name:
            self._patch_settings(script_name)

        return self.get_response(request)

    def _patch_settings(self, script_name):
        if not hasattr(settings, 'ORIG_STATIC_URL'):
            settings.ORIG_STATIC_URL = settings.STATIC_URL
            settings.STATIC_URL = script_name + settings.ORIG_STATIC_URL
        if not hasattr(settings, 'ORIG_MEDIA_URL'):
            settings.ORIG_MEDIA_URL = settings.MEDIA_URL
            settings.MEDIA_URL = script_name + settings.ORIG_MEDIA_URL
