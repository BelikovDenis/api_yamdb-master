from django.apps import AppConfig


class TitlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'titles'
    verbose_name = 'Произведение'
    verbose_name_plural = 'Произведения'
