from django.http import JsonResponse
from .models import ClientsLogos, ContactInformation, FewSuccessStories, GlobalExpansion, IndustriesWeServeCards, IndustriesWeServeDescription, ManagementTeam, MissionAndVision, OrganizationalStructureCards, OurPortfolioDescription, OurServicesDescription, PersonalImages, WhatSetsUsApartCards, about, service, stats
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


@require_http_methods(["GET"])
def management_team_json_view(request):
    try:
        management_team_members = ManagementTeam.objects.all()  # Fetch all team members
        if management_team_members.exists():
            data = {
                "management_team": [
                    {
                        "name": member.name,
                        "title": member.position,
                        "position": member.role,
                        "photo": member.image_url,
                        "description": member.about_text,
                        "socials" : {
                        "linkedin": member.linked_in_url,
                        },
                        
                    }
                    for member in management_team_members
                ]
            }
        else:
            data = {
                "error": "No management team members found."
            }
    except Exception as e:
        data = {
            "error": str(e)
        }
    return JsonResponse(data)

@require_http_methods(["GET"])
def personal_images_json_view(request):
    try:
        images = PersonalImages.objects.all()
        if images.exists():
            data = {
                "personal_images": [{"image_url": image.image_url} for image in images]
            }
        else:
            data = {"error": "No images found for Life at PaddleLift."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def our_services_description_json_view(request):
    try:
        services = OurServicesDescription.objects.all()
        if services.exists():
            data = {
                "our_services_descriptions": [
                    {"description": service.description} for service in services
                ]
            }
        else:
            data = {"error": "No services descriptions found."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def industries_we_serve_description_json_view(request):
    try:
        description = IndustriesWeServeDescription.objects.first()
        if description:
            data = {"description": description.description}
        else:
            data = {"error": "No description found for Industries We Serve."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def industries_we_serve_cards_json_view(request):
    try:
        cards = IndustriesWeServeCards.objects.all()
        if cards.exists():
            data = {
                "industries_we_serve_cards": [
                    {"name_of_industry": card.name_of_industry} for card in cards
                ]
            }
        else:
            data = {"error": "No cards found for Industries We Serve."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def what_sets_us_apart_cards_json_view(request):
    try:
        cards = WhatSetsUsApartCards.objects.first()
        if cards:
            data = {
                "what_sets_us_apart_cards": {
                    "card1": {"heading": cards.card1_heading, "description": cards.card1_description},
                    "card2": {"heading": cards.card2_heading, "description": cards.card2_description},
                    "card3": {"heading": cards.card3_heading, "description": cards.card3_description},
                    "card4": {"heading": cards.card4_heading, "description": cards.card4_description},
                }
            }
        else:
            data = {"error": "No cards found for What Sets Us Apart."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def organizational_structure_cards_json_view(request):
    try:
        cards = OrganizationalStructureCards.objects.first()
        if cards:
            data = {
                "organizational_structure_cards": {
                    "card1": {"heading": cards.card1_heading, "description": cards.card1_description},
                    "card2": {"heading": cards.card2_heading, "description": cards.card2_description},
                    "card3": {"heading": cards.card3_heading, "description": cards.card3_description},
                    "card4": {"heading": cards.card4_heading, "description": cards.card4_description},
                }
            }
        else:
            data = {"error": "No cards found for Organizational Structure."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def our_portfolio_description_json_view(request):
    try:
        description = OurPortfolioDescription.objects.first()
        if description:
            data = {"description": description.description}
        else:
            data = {"error": "No portfolio description found."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def few_success_stories_json_view(request):
    try:
        stories = FewSuccessStories.objects.all()
        if stories.exists():
            data = {
                "few_success_stories": [
                    {
                        "image_url": story.image_url,
                        "heading": story.heading,
                        "response": story.response,
                    }
                    for story in stories
                ]
            }
        else:
            data = {"error": "No success stories found."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)

@require_http_methods(["GET"])
def contact_information_json_view(request):
    try:
        contact = ContactInformation.objects.first()
        if contact:
            data = {
                "contact_information": {
                    "call": contact.call,
                    "WhatsApp": contact.WhatsApp,
                    "Email": contact.Email,
                    "Address": contact.Address,
                }
            }
        else:
            data = {"error": "No contact information found."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data)
