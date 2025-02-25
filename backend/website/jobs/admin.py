from django.contrib import admin
from .models import job_listing
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
# Register your models here.
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

from django import forms

class QuestionListWidget(forms.Textarea):
    class Media:
        css = {
            'all': ('/static/css/custom_admin.css',)
        }

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "question-widget",
            "placeholder": "Enter each question on a new line...",
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    
    def render(self, name, value, attrs=None, renderer=None):
        if value:
            value = "\n".join(value.split(" || "))  # Convert "||" to new lines
        return super().render(name, value, attrs, renderer)


class JobListingForm(forms.ModelForm):
    # Use TinyMCE widget for the Job_Description field
    Questions = forms.CharField(
        widget=QuestionListWidget(attrs={'rows': 5, 'placeholder': 'Enter each question on a new line...'}),
        required=False,
        help_text="Create Questions in new lines"
    )

    def clean_Questions(self):
        data = self.cleaned_data['Questions']
        return " || ".join(line.strip() for line in data.split("\n") if line.strip())  # Convert lines back to "||"
    
    
    class Meta:
        model = job_listing
        fields = '__all__'

    
    Job_Description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

@admin.register(job_listing)
class JobListingAdmin(ModelAdmin, ImportExportModelAdmin):
    form = JobListingForm  # Use the custom form with TinyMCE editor
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('Title','Work_Mode', 'Experience_level', 'Employment_type', 'Job_Location')

    def short_description(self, obj):
        return obj.Job_Description[:100] + '...' if obj.Job_Description else 'No Description'
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_save_and_continue'] = False # Here

        return super().changeform_view(request, object_id, form_url, extra_context)

    class Media:
        css = {
            "all": ("/static/css/q.css",)
        }
    
    short_description.short_description = 'Job Description'

