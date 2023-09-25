from __future__ import annotations

from typing import TYPE_CHECKING, Any, Sequence


import shutil
import typer

if TYPE_CHECKING:
    from manage_discord.context import Context


__all__: Sequence[str] = ("new_command_controller",)


def new_command_controller(ctx: Context) -> Any:
    ctx.project_location.mkdir(exist_ok=True)

    # Add the base files to the new project
    shutil.copytree(ctx.base, ctx.project_location, dirs_exist_ok=True)

    # Create the /bot folder in the project directory and add the bot files
    bot_dir = ctx.project_location / "bot"
    bot_dir.mkdir(exist_ok=True)
    shutil.copytree(ctx.bot_path, bot_dir, dirs_exist_ok=True)

    typer.echo(
        f"{typer.style('Successfully created your new project!', fg='bright_blue')}"
    )