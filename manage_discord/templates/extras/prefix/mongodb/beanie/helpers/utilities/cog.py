from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Sequence, Tuple

from helpers.errors import InvalidCogsDirectory

if TYPE_CHECKING:
    from helpers.config import Config

__all__: Sequence[str] = ("get_cogs", "get_absolute_cogs_dir", "is_valid_cog")


def get_cogs(config: Config) -> Tuple[str, ...]:
    """
    Get a tuple of cog paths.
    Scans the cogs directory for valid cogs and returns their paths.
    """
    cogs: Tuple[str, ...] = tuple()

    cogs_directory = get_absolute_cogs_dir(config)
    for x in cogs_directory.iterdir():
        if is_valid_cog(x):
            cogs = cogs + (f"{config.cogs_directory}.{x.name}.{x.name.lower()}",)
    return cogs


def get_absolute_cogs_dir(config: Config) -> Path:
    """Get the absolute path to the cogs directory."""
    cogs_directory = (
        Path(os.path.realpath(os.path.dirname("bot/"))) / config.cogs_directory
    )
    if not cogs_directory.is_dir():
        raise InvalidCogsDirectory(
            f"The specified cog directory {cogs_directory!r} is not a valid directory."
        )
    return cogs_directory


def is_valid_cog(directory: Path) -> bool:
    """Check if a directory is a valid cog."""
    return (
        directory.is_dir()
        and not directory.name.startswith("_")
        and f"{directory.name.lower()}"
        in (i.stem for i in directory.iterdir() if i.name.endswith(".py"))
    )
