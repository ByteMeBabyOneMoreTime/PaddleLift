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



class JobListingForm(forms.ModelForm):
    # Use TinyMCE widget for the Job_Description field
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

    short_description.short_description = 'Job Description'

