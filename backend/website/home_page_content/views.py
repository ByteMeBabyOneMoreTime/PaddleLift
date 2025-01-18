from django.http import JsonResponse
from .models import service

def get_service_data(request: object) -> JsonResponse:
    """
    Returns the Json Get Data of the Services Section Component
    """
    if request.method == "GET":
        try:
            # Retrieve the single instance of the service model
            service_instance = service.objects.get()
            data = {
                "service1": {
                    "id" : "1",
                    "heading": service_instance.service1_heading,
                    "vedio_url": service_instance.service1_vedio_url,
                },
                "service2": {
                    "id" : "2",
                    "heading": service_instance.service2_heading,
                    "vedio_url": service_instance.service2_vedio_url,
                },
                "service3": {
                    "id" : "3",
                    "heading": service_instance.service3_heading,
                    "vedio_url": service_instance.service3_vedio_url,
                },
                "service4": {
                    "id" : "4",
                    "heading": service_instance.service4_heading,
                    "vedio_url": service_instance.service4_vedio_url,
                },
            }
            return JsonResponse(data, status=200)
        except service.DoesNotExist:
            return JsonResponse({"error": "Service data not found"}, status=404)
    else:
        return JsonResponse({"error": "This method is not allowed"}, status=405)