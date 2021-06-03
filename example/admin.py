from django.contrib import admin

from example.forms import PeopleAdminForm
from example.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    form = PeopleAdminForm

    def save_model(self, request, obj, form, change):
        print(obj.languages)

        super().save_model(request, obj, form, change)
