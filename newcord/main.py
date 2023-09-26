from __future__ import annotations

import os
from typing import Sequence

import typer

from newcord.context import Context
from newcord.controllers import new_command_controller
from newcord.helpers import (
    get_template_dir,
    create_project_path,
    select_from_directory,
    confirm,
)

__all__: Sequence[str] = ("app",)


app = typer.Typer(name="newcord")


@app.command(name="new")
def new_command():
    typer.clear()

    project_path = create_project_path()
    template_dir = get_template_dir()
    extras_dir = os.path.join(template_dir, "extras")

    extras_dir = os.path.join(
        extras_dir, select_from_directory("Choose a command type", extras_dir)
    )

    if confirm("Would you like to integrate a database into your project"):
        for question in [
            "Select the type of database you want to use",
            "Choose a database driver or library for your selected database",
        ]:
            extras_dir = os.path.join(
                extras_dir, select_from_directory(question, extras_dir)
            )
    else:
        extras_dir = os.path.join(extras_dir, "_no-database")

    new_command_controller(
        Context(
            project_location=project_path,
            base=os.path.join(template_dir, "base"),
            bot_path=extras_dir,
        )
    )


@app.command(name="cog")
def cog_command():
    ...


if __name__ == "__main__":
    app()
