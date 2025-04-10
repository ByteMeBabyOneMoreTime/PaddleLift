from django.urls import path

from .views import (
    about_json_view,
    clients_logos_view,
    contact_information_json_view,
    few_success_stories_json_view,
    get_service_data,
    global_expansion_view,
    industries_we_serve_cards_json_view,
    industries_we_serve_description_json_view,
    management_team_json_view,
    mission_and_vision_json_view,
    organizational_structure_cards_json_view,
    our_portfolio_description_json_view,
    our_services_description_json_view,
    personal_images_json_view,
    reviews_json_view,
    stats_view,
    what_our_clients_say_json_view,
    what_sets_us_apart_cards_json_view,
)

urlpatterns = [
    path("get-service/", get_service_data, name="get_service_data"),
    path(
        "operations-around-the-world/", global_expansion_view, name="global-expansion"
    ),
    path("our-statistics/", stats_view, name="stats"),
    path("clients/", view=clients_logos_view, name="clients"),
    path("about/", about_json_view, name="about"),
    path(
        "mission-and-vision/", mission_and_vision_json_view, name="mission_and_vision"
    ),
    path("management/", management_team_json_view, name="management"),
    path("personal-images/", personal_images_json_view, name="personal-images"),
    path("our-services/", our_services_description_json_view, name="our-services"),
    path(
        "industries-description/",
        industries_we_serve_description_json_view,
        name="industries-description",
    ),
    path(
        "industries-cards/",
        industries_we_serve_cards_json_view,
        name="industries-cards",
    ),
    path(
        "what-sets-us-apart/",
        what_sets_us_apart_cards_json_view,
        name="what-sets-us-apart",
    ),
    path(
        "organizational-structure/",
        organizational_structure_cards_json_view,
        name="organizational-structure",
    ),
    path(
        "portfolio-description/",
        our_portfolio_description_json_view,
        name="portfolio-description",
    ),
    path(
        "few-success-stories/",
        few_success_stories_json_view,
        name="few-success-stories",
    ),
    path(
        "contact-information/",
        contact_information_json_view,
        name="contact-information",
    ),
    path("reviews", reviews_json_view, name="reviews"),
    path(
        "what-our-clients-say/",
        what_our_clients_say_json_view,
        name="what-our-clients-say",
    ),
]
