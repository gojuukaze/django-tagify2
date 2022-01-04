from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.templatetags.static import static


class TagInput(forms.TextInput):
    class Media:
        js = (static("tagify/js/tagify.min.js"),)
        css = {"all": (static("tagify/css/tagify.css"),)}

    template_name = "tagify/tagify_input.html"
    tag_args = {}
    var_name = None
    

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["type"] = self.input_type
        context["widget"]["var_name"] = getattr(self, "var_name", None)
        context["widget"]["tag_args"] = getattr(self, "tag_args", None) or {
            "placeholder": "write some tags",
            "delimiters": ",",
            "pattern": "/^.*$/",
            "whitelist": [],
            "suggestionsMinChars": 1,
            "blacklist": [],
            "maxTags": None,
        }
        return context
