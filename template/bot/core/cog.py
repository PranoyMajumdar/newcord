from __future__ import annotations


from typing import TYPE_CHECKING, Sequence
from discord.ext import commands

if TYPE_CHECKING:
    from .bot import Bot

__all__: Sequence[str] = (
    "Cog",
)


class Cog(commands.Cog):
    """A custom implementation of commands.Cog."""
    def __init__(self, bot: Bot) -> None:
        super().__init__()
