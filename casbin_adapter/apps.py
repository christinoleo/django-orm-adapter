from django.apps import AppConfig
from django.conf import settings
from asgiref import sync_to_async
import asyncio


async def setup():
    from .enforcer import initialize_enforcer

    db_alias = getattr(settings, "CASBIN_DB_ALIAS", "default")
    await sync_to_async(initialize_enforcer)(db_alias)


class CasbinAdapterConfig(AppConfig):
    name = "casbin_adapter"

    def ready(self):
        asyncio.create_task(setup())
