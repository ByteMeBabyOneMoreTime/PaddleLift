from django.http import JsonResponse
from .models import *
from django.views.decorators.http import require_http_methods

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
                    "vedio_url": service_instance.service1_video_url,
                },
                "service2": {
                    "id" : "2",
                    "heading": service_instance.service2_heading,
                    "vedio_url": service_instance.service2_video_url,
                },
                "service3": {
                    "id" : "3",
                    "heading": service_instance.service3_heading,
                    "vedio_url": service_instance.service3_video_url,
                },
                "service4": {
                    "id" : "4",
                    "heading": service_instance.service4_heading,
                    "vedio_url": service_instance.service4_video_url,
                },
            }
            return JsonResponse(data, status=200)
        except service.DoesNotExist:
            return JsonResponse({"error": "Service data not found"}, status=404)
    else:
        return JsonResponse({"error": "This method is not allowed"}, status=405)
    

@require_http_methods(["GET"])
def global_expansion_view(request):
    """
    Handle GET requests to retrieve Global Expansion details.
    """
    try:
        # Get the first instance of GlobalExpansion (Singleton pattern)
        global_expansion = GlobalExpansion.objects.first()
        
        if not global_expansion:
            return JsonResponse(
                {"error": "Global Expansion data not found."},
                status=404
            )

        # Return the data as JSON
        data = {
            "description": global_expansion.description,
        }
        return JsonResponse(data, status=200)

    except Exception as e:
        # Handle unexpected errors
        return JsonResponse(
            {"error": "An error occurred while retrieving the data.", "details": str(e)},
            status=500
        )
    

@require_http_methods(["GET"])
def stats_view(request):
    """
    Handle GET requests to retrieve stats data.
    """
    try:
        # Get the first instance of stats (Singleton pattern)
        stats_instance = stats.objects.first()
        
        if not stats_instance:
            return JsonResponse(
                {"error": "Stats data not found."},
                status=404
            )

        # Return the stats data as JSON
        data = {
            "id": stats_instance.id,
            "description": stats_instance.description,
            "ClientsServed": stats_instance.ClientsServed,
            "CandidatesPlaced": stats_instance.CandidatesPlaced,
            "ClientRetentionRate": stats_instance.ClientRetentionRate,
            "TurnAroundTime": stats_instance.TurnAroundTime,
            "JoiningRatio": stats_instance.JoiningRatio,
            "CandidateSatisfactionRate": stats_instance.CandidateSatisfactionRate,
        }
        return JsonResponse(data, status=200)

    except Exception as e:
        # Handle unexpected errors
        return JsonResponse(
            {"error": "An error occurred while retrieving the stats.", "details": str(e)},
            status=500
        )