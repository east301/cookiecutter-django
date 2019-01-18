#
#
#

from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = '{{cookiecutter.package_name}}.apps.account'

    def ready(self):
        import {{cookiecutter.package_name}}.apps.account.handlers   # NOQA
