from __future__ import annotations

from typing import Sequence

from discord import DiscordException

__all__: Sequence[str] = ("InvalidCogsDirectory",)


class InvalidCogsDirectory(DiscordException):
    """The cogs folder pattern is invalid."""
