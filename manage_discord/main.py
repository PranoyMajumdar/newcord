from __future__ import annotations
from typing import Any, Callable, Sequence
from pathlib import Path
import typer
import os
import questionary
from manage_discord.controllers import new_command_controller
from manage_discord.helpers import style
from manage_discord.context import Context


__all__: Sequence[str] = ("app",)
app = typer.Typer(name="manage-discord")


def select_from_directory(prompt, directory):
    check: Callable[[str], Any] = lambda x: not x.startswith("_")

    return (
        questionary.select(
            message=prompt,
            choices=list(i.capitalize() for i in filter(check, os.listdir(directory))),
            style=style,
            pointer="❯",
        )
        .unsafe_ask()
        .lower()
    )



def ask_question(prompt, default="project"):
    return questionary.text(
        message=prompt, style=style, default=default
    ).unsafe_ask()


@app.command(name="new")
def new_command():
    typer.clear()

    project_path = Path(ask_question("Where do we create your project"))

    template_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "templates"
    )
    extras_dir = os.path.join(template_dir, "extras")

    extras_dir = os.path.join(
        extras_dir, select_from_directory("Choose a command type", extras_dir)
    )
    if questionary.confirm(
        message="Do you want to use database", style=style
    ).unsafe_ask():
        for question in [
            "Select a database",
            "Select a database driver",
        ]:
            extras_dir = os.path.join(
                extras_dir, select_from_directory(question, extras_dir)
            )
    else:
        extras_dir = os.path.join(extras_dir, "no-database")

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
