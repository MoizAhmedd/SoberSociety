from django.apps import AppConfig


class OpenbookConfig(AppConfig):
    name = 'Openbook'

    def ready(self):
        import Openbook.signals
