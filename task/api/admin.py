from django.contrib import admin
from django.apps import apps

class CustomAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [fields.name for fields in model._meta.fields]

        super().__init__(model, admin_site)


models = apps.get_models()

from django.contrib import auth

for model in models:
    try:
        if model not in (auth.models.Group, auth.models.User):
            admin.site.register(model, CustomAdmin)
    except admin.sites.AlreadyRegistered:
        pass