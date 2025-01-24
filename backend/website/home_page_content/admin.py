from django.contrib import admin
from django import forms
from .models import MissionAndVision, about, stats, ClientsLogos, GlobalExpansion, service, ClientsResponse
from website.settings import HOME_PAGE_CONTENT_FOLDER
from cloud.utils import file_url
import imghdr
from django.core.exceptions import ValidationError

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
    image = forms.ImageField(validators=[validate_image], required=True)

    class Meta:
        model = ClientsLogos
        fields = ['name','image']
        exclude = ['logo_url']

class ClientsLogosAdmin(admin.ModelAdmin):
    form = ClientsLogosAdminForm
    list_display = ('name', 'logo_url')
    readonly_fields = ('logo_url',)

    def has_change_permission(self, request, obj=None):
        if obj is None and ClientsLogos.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in obj._meta.fields]
        return super().get_readonly_fields(request, obj)
    
    def save_model(self, request, obj, form, change):
        if 'image' in form.cleaned_data:
            file = form.cleaned_data['image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.logo_url = url  
        super().save_model(request, obj, form, change)


class ClientsResponsesAdminForm(forms.ModelForm):
    image = forms.ImageField(validators=[validate_image], required=True)

    class Meta:
        model = ClientsResponse
        fields = ['name','position', 'response','image' ]
        exclude = ['image_url']

class ClientsResponsesAdmin(admin.ModelAdmin):
    form = ClientsResponsesAdminForm
    list_display = ('name', 'image_url', 'position', 'response')
    readonly_fields = ('image_url',)

    def has_change_permission(self, request, obj=None):
        if obj is None and ClientsResponse.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in obj._meta.fields]
        return super().get_readonly_fields(request, obj)
    
    def save_model(self, request, obj, form, change):
        if 'image' in form.cleaned_data:
            file = form.cleaned_data['image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.image_url = url  
        super().save_model(request, obj, form, change)

class MissionAndVisionAdminForm(forms.ModelForm):
    vission_image = forms.ImageField(validators=[validate_image], required=True)
    mission_image = forms.ImageField(validators=[validate_image], required=True)

    class Meta:
        model = MissionAndVision
        fields = ['vission_image' ,'vission_description' ,'mission_image' ,'mission_description']
        exclude = ['vission_image_url', 'mission_image_url']

class MissionAndVisionAdmin(admin.ModelAdmin):
    form = MissionAndVisionAdminForm
    list_display = ('vission_image_url' ,'vission_description' ,'mission_image_url' ,'mission_description')
    readonly_fields = ('vission_image_url', 'mission_image_url')

    def has_change_permission(self, request, obj=None):
        if obj is None and MissionAndVision.objects.exists():
            return False
        return super().has_change_permission(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in obj._meta.fields]
        return super().get_readonly_fields(request, obj)
    
    def save_model(self, request, obj, form, change):
        if 'vission_image' in form.cleaned_data:
            file = form.cleaned_data['vission_image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.vission_image_url = url  
        if 'mission_image' in form.cleaned_data:
            file = form.cleaned_data['mission_image']
            url = file_url(file, folder_id=HOME_PAGE_CONTENT_FOLDER, file_type=1)
            obj.mission_image_url = url  
        
        super().save_model(request, obj, form, change)

admin.site.register(service)
admin.site.register(GlobalExpansion)
admin.site.register(stats)
admin.site.register(ClientsLogos, ClientsLogosAdmin)
admin.site.register(ClientsResponse, ClientsResponsesAdmin)
admin.site.register(about)
admin.site.register(MissionAndVision, MissionAndVisionAdmin)