from django.contrib import admin
from django import forms

from django.db import models
from .models import ManagementTeam, MissionAndVision, about, stats, ClientsLogos, GlobalExpansion, service, ClientsResponse
from website.settings import HOME_PAGE_CONTENT_FOLDER
from cloud.utils import file_url
import imghdr
from django.core.exceptions import ValidationError
from unfold.admin import ModelAdmin
from image_uploader_widget.widgets import ImageUploaderWidget

def validate_image(value):
    """
    Validates if the uploaded file is a valid image (JPG, JPEG, PNG, or GIF)
    """
    try:
        # Check if file was uploaded
        if not value:
            raise ValidationError("No file was submitted.")
        
        # Map imghdr's return values to file extensions
        valid_image_types = {
            'jpeg': ['jpg', 'jpeg'],
            'png': ['png'],
            'gif': ['gif']
        }
        
        # Get the file extension
        ext = value.name.split('.')[-1].lower()
        
        # Check the actual content of the file
        try:
            file_type = imghdr.what(value.file)
        except AttributeError:
            file_type = imghdr.what(value)
            
        if file_type is None:
            raise ValidationError("Uploaded file is not a valid image.")
        
        # Check if the detected type matches acceptable formats
        valid_extensions = []
        for img_type, extensions in valid_image_types.items():
            valid_extensions.extend(extensions)
            if file_type == img_type and ext in extensions:
                return value
                
        raise ValidationError(
            f"Invalid image format. Detected format: {file_type}. "
            f"Allowed formats: {', '.join(valid_extensions)}"
        )
    except Exception as e:
        raise ValidationError(f"Validation error: {str(e)}")





class ClientsLogosAdminForm(forms.ModelForm):
    image = forms.ImageField(validators=[validate_image], required=False, widget=ImageUploaderWidget())

    class Meta:
        model = ClientsLogos
        fields = ['name','image']
        exclude = ['logo_url']

@admin.register(ClientsLogos)
class ClientsLogosAdmin(ModelAdmin):
    form = ClientsLogosAdminForm
    list_display = ('name', 'logo_url')
    readonly_fields = ('logo_url',)

    def has_change_permission(self, request, obj=None):
        if obj is None and ClientsLogos.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    
    def save_model(self, request, obj, form, change):
        if 'image' in form.cleaned_data and form.cleaned_data['image']:
            file = form.cleaned_data['image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.logo_url = url  
        super().save_model(request, obj, form, change)


class ClientsResponsesAdminForm(forms.ModelForm):
    image = forms.ImageField(validators=[validate_image], required=False,  widget=ImageUploaderWidget())

    class Meta:
        model = ClientsResponse
        fields = ['name','position', 'response','image' ]
        exclude = ['image_url']

@admin.register(ClientsResponse)
class ClientsResponsesAdmin(ModelAdmin):
    form = ClientsResponsesAdminForm
    list_display = ('name', 'image_url', 'position', 'response')
    readonly_fields = ('image_url',)

    def has_change_permission(self, request, obj=None):
        if obj is None and ClientsResponse.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    
    def save_model(self, request, obj, form, change):
        if 'image' in form.cleaned_data and form.cleaned_data['image']:
            file = form.cleaned_data['image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.image_url = url  
        super().save_model(request, obj, form, change)

class MissionAndVisionAdminForm(forms.ModelForm):
    vission_image = forms.ImageField(validators=[validate_image], required=False,  widget=ImageUploaderWidget())
    mission_image = forms.ImageField(validators=[validate_image], required=False,  widget=ImageUploaderWidget())

    class Meta:
        model = MissionAndVision
        fields = ['vission_image' ,'vission_description' ,'mission_image' ,'mission_description']
        exclude = ['vission_image_url', 'mission_image_url']

@admin.register(MissionAndVision)
class MissionAndVisionAdmin(ModelAdmin):
    form = MissionAndVisionAdminForm
    list_display = ('vission_image_url' ,'vission_description' ,'mission_image_url' ,'mission_description')
    readonly_fields = ('vission_image_url', 'mission_image_url')

    def has_change_permission(self, request, obj=None):
        if obj is None and MissionAndVision.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    def save_model(self, request, obj, form, change):
        if 'vission_image' in form.cleaned_data and form.cleaned_data['vission_image']:
            file = form.cleaned_data['vission_image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.vission_image_url = url  
        if 'mission_image' in form.cleaned_data and form.cleaned_data['mission_image']:
            file = form.cleaned_data['mission_image'] 
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.mission_image_url = url  
        
        super().save_model(request, obj, form, change)

class ManagementTeamAdminForm(forms.ModelForm):
    image = forms.ImageField(validators=[validate_image], required=False,  widget=ImageUploaderWidget())

    class Meta:
        model = ManagementTeam
        fields = ['name','position','role','linked_in_url', 'about_text', 'image' ]
        exclude = ['image_url']

@admin.register(ManagementTeam)
class ManagementTeamAdmin(admin.ModelAdmin):
    form = ManagementTeamAdminForm
    list_display = ('name','position','role','linked_in_url', 'about_text', 'image_url')
    readonly_fields = ('image_url',)

    def has_change_permission(self, request, obj=None):
        if obj is None and ManagementTeam.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    
    def save_model(self, request, obj, form, change):
        if 'image' in form.cleaned_data and form.cleaned_data['image']:
            file = form.cleaned_data['image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.image_url = url  
        super().save_model(request, obj, form, change)


@admin.register(service)
class Serivice(ModelAdmin):
    pass

@admin.register(GlobalExpansion)
class GlobalExpansion(ModelAdmin):
    pass

@admin.register(stats)
class stats(ModelAdmin):
    pass

@admin.register(about)
class about(ModelAdmin):
    pass

