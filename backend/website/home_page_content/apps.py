from django.apps import AppConfig


class HomePageContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_page_content'
    verbose_name = 'Website content components '
    def ready(self):
        import home_page_content.siganls