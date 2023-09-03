from __future__ import annotations

import discord

from typing import Any, Sequence
from discord.ext import commands
from logging import getLogger

__all__: Sequence[str] = ("Bot",)


log = getLogger(__name__)


class Bot(commands.AutoShardedBot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            case_insensitive=True,
            description="A template generated using manage-dpy tool.",
        )

    async def setup_hook(self) -> Any:
        return NotImplemented

    async def on_ready(self) -> Any:
        assert self.user is not None
        return log.info(f"Logged in as {self.user.name} (ID: {self.user.id})")
