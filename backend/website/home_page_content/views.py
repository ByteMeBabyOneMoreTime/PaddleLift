from django.http import JsonResponse
from .models import ClientsLogos, GlobalExpansion, MissionAndVision, about, service, stats
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
            "data":   [{
                    "title": "Clients Served",
                    "value": stats_instance.ClientsServed,
                    "suffix": "+",
                },
                {
                    "title": "Candidates Placed",
                    "value": stats_instance.CandidatesPlaced,
                    "suffix": "+",
                },
                {
                    "title": "Client Retention Rate (CRR)",
                    "prefix": ">",
                    "value": stats_instance.ClientRetentionRate,
                    "suffix": "%",
                },
                {
                    "title": "Turn Around Time (TAT)",
                    "prefix": "<",
                    "value": stats_instance.TurnAroundTime,
                    "suffix": "Hrs",
                },
                {
                    "title": "Joining Ratio",
                    "prefix": ">",
                    "value": stats_instance.JoiningRatio,
                    "suffix": "%",
                },
                {
                    "title": "Candidate Satisfaction Rate (CSR)",
                    "prefix": ">",
                    "value": stats_instance.CandidateSatisfactionRate,
                    "suffix": "%",
                }
            ],
        }
        return JsonResponse(data, status=200)

    except Exception as e:
        # Handle unexpected errors
        return JsonResponse(
            {"error": "An error occurred while retrieving the stats.", "details": str(e)},
            status=500
        )
    


@require_http_methods(["GET"])
def clients_logos_view(request):
    """
    Handle GET requests to retrieve all Client Logos details.
    """
    try:
        # Retrieve all client logos from the database
        clients_logos = ClientsLogos.objects.all()

        if not clients_logos.exists():
            return JsonResponse(
                {"error": "No client logos found."},
                status=404
            )

        # Serialize the data into a list of dictionaries
        data = [
            {   "id" : client_logo.id,
                "src": client_logo.logo_url,
                "name": client_logo.name,
                
            }
            for client_logo in clients_logos
        ]

        return JsonResponse({"clients_logos": data}, status=200)

    except Exception as e:
        # Handle unexpected errors
        return JsonResponse(
            {"error": "An error occurred while retrieving the data.", "details": str(e)},
            status=500
        )


@require_http_methods(["GET"])
def about_json_view(request):
    try:
        about_instance = about.objects.first()
        if about_instance:
            data = {
                "description": about_instance.description,
            }
        else:
            data = {
                "error": "No 'About PaddleLift' instance found."
            }
    except Exception as e:
        data = {
            "error": str(e)
        }
    return JsonResponse(data)


@require_http_methods(["GET"])
def mission_and_vision_json_view(request):
    try:
        mission_and_vision_instance = MissionAndVision.objects.first()  # Fetching the singleton instance
        if mission_and_vision_instance:
            data = {
                "vision": {
                    "image_url": mission_and_vision_instance.vission_image_url,
                    "description": mission_and_vision_instance.vission_description,
                },
                "mission": {
                    "image_url": mission_and_vision_instance.mission_image_url,
                    "description": mission_and_vision_instance.mission_description,
                }
            }
        else:
            data = {
                "error": "No 'Mission and Vision' instance found."
            }
    except Exception as e:
        data = {
            "error": str(e)
        }
    return JsonResponse(data)