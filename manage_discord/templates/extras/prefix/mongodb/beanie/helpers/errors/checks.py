from __future__ import annotations

from typing import Sequence

from discord.ext import commands


__all__: Sequence[str] = ("NotBotOwner", "NotGuildOwner", "NotGuildAdmin")


class NotBotOwner(commands.CheckFailure):
    """Only bot owner can use this command."""


class NotGuildOwner(commands.CheckFailure):
    """Only guild owner can use this command."""


class NotGuildAdmin(commands.CheckFailure):
    """Only guild admin(s) can use this command."""
