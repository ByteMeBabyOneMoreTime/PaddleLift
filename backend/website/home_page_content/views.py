from django.http import JsonResponse
from .models import service

def get_service_data(request):
    try:
        # Retrieve the single instance of the service model
        service_instance = service.objects.get()
        data = {
            "service1": {
                "heading": service_instance.service1_heading,
                "image_url": service_instance.service1_image_url,
            },
            "service2": {
                "heading": service_instance.service2_heading,
                "image_url": service_instance.service2_image_url,
            },
            "service3": {
                "heading": service_instance.service3_heading,
                "image_url": service_instance.service3_image_url,
            },
            "service4": {
                "heading": service_instance.service4_heading,
                "image_url": service_instance.service4_image_url,
            },
        }
        return JsonResponse(data, status=200)
    except service.DoesNotExist:
        return JsonResponse({"error": "Service data not found"}, status=404)
