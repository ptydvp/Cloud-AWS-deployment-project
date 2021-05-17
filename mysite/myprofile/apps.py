from django.apps import AppConfig


class MyprofileConfig(AppConfig):
    name = 'myprofile'

    def ready(self):
        import myprofile.signals