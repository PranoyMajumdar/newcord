from __future__ import annotations

from typing import TYPE_CHECKING, Any

from discord.ext import commands
from helpers import errors
from core import Cog

if TYPE_CHECKING:
    from core import Bot, Context

class ErrorsCog(Cog, name="Errors"):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    
    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception) -> Any:
        ignore = (
            commands.CommandNotFound,
        )

        if isinstance(error, ignore):
            return
        
        if isinstance(error, commands.CheckFailure):
            if isinstance(error, errors.NotBotOwner):
                return await ctx.error("Only bot owner(s) can use this command.")
            if isinstance(error, errors.NotGuildOwner):
                return await ctx.error(f"Only {f'<@{ctx.guild.owner_id}>' if ctx.guild else 'owner(s)'} can use this command.")
            if isinstance(error, errors.NotGuildAdmin):
                return await ctx.error("Only member with administration permission can use this command.")

async def setup(bot: Bot) -> None:
    await bot.add_cog(ErrorsCog(bot))