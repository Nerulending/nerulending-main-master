from django.apps import apps
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

app = apps.get_app_config('affiliate')


for model in app.get_models():
    admin.site.register(model)
