#
#
#

from django.contrib import admin


# ================================================================================
# django admin title
# ================================================================================

admin.site.site_header = '{{cookiecutter.package_name}} Administration'
admin.site.site_title = admin.site.site_header
