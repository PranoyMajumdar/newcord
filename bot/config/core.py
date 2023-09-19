from __future__ import annotations

from typing import Final, List, Sequence, Tuple, Union
from dataclasses import dataclass, field

from .database import DatabaseConfig

__all__: Sequence[str] = ("Config",)


@dataclass
class Config:
    # Bot configurations
    token: Final[str] = "Your bot token"
    prefix: Final[str] = "!"

    # Cogs configurations
    cogs_directory: Final[str] = "cogs"
    cogs: Final[Tuple[str, ...]] = ("Admin",)

    # Database config
    database: DatabaseConfig = field(default_factory=lambda: DatabaseConfig(
        uri="Your mongodb uri",
        name="main"
    ))

    @property
    def db(self) -> DatabaseConfig:
        return self.database
