from __future__ import annotations

from typing import TYPE_CHECKING
from core import Cog


if TYPE_CHECKING:
    from core import Bot


class AdminCog(Cog, name="Admin"):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot


async def setup(bot: Bot) -> None:
    await bot.add_cog(AdminCog(bot))
