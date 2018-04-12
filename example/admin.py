
from django.contrib import admin

from example.forms import PeopleAdminForm
from example.models import People
from ktag.admin import MultipleChoiceAdmin


@admin.register(People)
class PeopleAdmin(MultipleChoiceAdmin):
    form = PeopleAdminForm

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)
        """
        filter fruits from PeopleFruits
        PeopleFruits.objects.filter(people_id=object_id)
        ...
        """
        # bind value
        self.choice_field_value['fruits'] = "grape,coconut"
        return obj

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        fruits = form.cleaned_data['fruits']
        print(fruits)
        for f in fruits:
            """
            save PeopleFruits
            ...
            PeopleFruits(people_id=obj.id,fruit=f).save()
            ...
            """
            pass
