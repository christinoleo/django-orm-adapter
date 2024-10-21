from django.apps import AppConfig
from django.conf import settings
from asgiref import sync_to_async


class CasbinAdapterConfig(AppConfig):
    name = "casbin_adapter"

    def ready(self):
        from .enforcer import initialize_enforcer

        db_alias = getattr(settings, "CASBIN_DB_ALIAS", "default")
        sync_to_async(initialize_enforcer)(db_alias)
