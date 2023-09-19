from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Sequence


__all__: Sequence[str] = ("DatabaseConfig",)


@dataclass
class DatabaseConfig:
    uri: str
    name: str
    
