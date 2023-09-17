from __future__ import annotations

from typing import Final, List, Tuple, Union

from dataclasses import dataclass


@dataclass
class Config:
    # Bot configurations
    token: Final[str] = "Your Bot Token"
    prefix: Final[Union[str, List[str]]] = "!"

    # Cogs configurations
    cogs_directory: Final[str] = "cogs"
    cogs: Final[Tuple[str, ...]] = ("Admin",)
