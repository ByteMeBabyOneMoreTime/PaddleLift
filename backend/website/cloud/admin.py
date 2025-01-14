from django.contrib import admin
from django import forms
from .models import CV
from django.conf import settings
from .utils import file_url

class CVAdminForm(forms.ModelForm):
    file = forms.FileField()
    
    class Meta:
        model = CV
        fields = ['name', 'email', 'phone_no', 'file']
        exclude = ['cv_url']

class CVAdmin(admin.ModelAdmin):
    form = CVAdminForm
    list_display = ('name','email', 'phone_no', 'cv_url', 'uploaded_at')
    readonly_fields = ('cv_url', 'uploaded_at')

    def save_model(self, request, obj, form, change):
        file = form.cleaned_data['file']
        
        url = file_url(file, settings.CV_FOLDER, file_type=0)
        obj.cv_url = url
        super().save_model(request, obj, form, change)

admin.site.register(CV, CVAdmin)