from typing import Type

from ayon_server.addons import BaseServerAddon

from .settings import DeadlineSettings, DEFAULT_VALUES


class Deadline(BaseServerAddon):
    settings_model: Type[DeadlineSettings] = DeadlineSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
