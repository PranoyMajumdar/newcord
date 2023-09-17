from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Any, Sequence

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from configs import Config

__all__: Sequence[str] = ("Bot",)


log = getLogger(__name__)


class Bot(commands.AutoShardedBot):
    def __init__(self, config: Config, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or(*config.cogs),
            intents=discord.Intents.all(),
            case_insensitive=True,
            description="A template generated using manage-dpy tool.",
        )
        self.config = config

    async def load_cogs(self) -> None:
        for cog in self.config.cogs:
            try:
                await self.load_extension(f"{self.config.cogs_directory}.{cog}.cog")
                log.info(f"Successfully loaded {cog!r} cog.")
            except Exception as exc:
                log.error(
                    f"Could not load extension {cog} {exc.__class__.__name__}: {exc}"
                )

    async def setup_hook(self) -> Any:
        await self.load_cogs()

    async def on_ready(self) -> Any:
        assert self.user is not None
        return log.info(f"Logged in as {self.user.name} (ID: {self.user.id})")

    async def start(self) -> None: # type: ignore
        return await super().start(self.config.token, reconnect=True)
