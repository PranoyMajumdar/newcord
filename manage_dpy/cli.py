from __future__ import annotations


import typing
import typer
import questionary


if typing.TYPE_CHECKING:
    ...


app = typer.Typer(name="discord")


@app.command(name="init")
def init_command():
    answers = questionary.form(
        directory=questionary.text(message="What will be the project directory for your bot"),
        package_manager=questionary.select(
            message="Choose a package manager for your project", choices=["PIP", "Poetry"]
        ),
        database=questionary.select(
            message="Select a database toolkit for your bot",
            choices=["asyncpg",
                "Tortoise-ORM",
                "SQLAlchemy",
                "Beanie",
                "None",],
            default="SQLAlchemy",
        ),
        features=questionary.checkbox(
            message="Choose utility features you'd like to include",
            choices=['Paginator', 'Custom Context', 'View']
        ),
        mypy=questionary.confirm(message="Would you like to use Mypy for type checking", default=True),
        black=questionary.confirm(message="Would you like to use the Black code formatter", default=True),
        slashcommands=questionary.confirm(message="Do you want to enable Slash Commands or Hybrid Commands in your bot", default=True)
    ).ask()
    print(answers)
