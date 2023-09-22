from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from discord.ext import commands
from helpers.errors import NotBotOwner, NotGuildOwner, NotGuildAdmin

if TYPE_CHECKING:
    from core.context import Context
    from discord import User
    from discord.ext.commands._types import Check

__all__: Sequence[str] = ("is_owner", "is_guild_owner", "is_guild_admin")


def is_owner() -> Check:
    async def predicate(ctx: Context) -> bool:
        if not ctx.bot.owner_ids or ctx.author.id not in ctx.bot.owner_ids:
            raise NotBotOwner()

        return True

    return commands.check(predicate)


def is_guild_owner() -> Check:
    async def predicate(ctx: Context) -> bool:
        if ctx.guild is None or ctx.guild.owner_id == ctx.author.id:
            return True

        raise NotGuildOwner()

    return commands.check(predicate)


def is_guild_admin() -> Check:
    async def predicate(ctx: Context) -> bool:
        if (
            ctx.guild is None
            or isinstance(ctx.author, User)
            or ctx.author.guild_permissions.administrator
        ):
            return True

        raise NotGuildAdmin()

    return commands.check(predicate)
