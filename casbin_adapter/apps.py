from django.apps import AppConfig
from django.conf import settings
from asgiref.sync import sync_to_async
import asyncio


async def setup():
    from .enforcer import initialize_enforcer

    db_alias = getattr(settings, "CASBIN_DB_ALIAS", "default")
    await sync_to_async(initialize_enforcer)(db_alias)


class CasbinAdapterConfig(AppConfig):
    name = "casbin_adapter"

    def ready(self):
        try:
            asyncio.create_task(setup())
        except RuntimeError:
            # running dev server
            import warnings

            warnings.filterwarnings("ignore", category=RuntimeWarning, module="pygments")
            asyncio.run(setup())
