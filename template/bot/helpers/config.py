from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from logging import getLogger

__all__: Sequence[str] = (
    "Configs",
)


log = getLogger(__name__)

@dataclass
class Configs:
    """This class provides and validates the configs.json file."""

    def __post__init__(self) -> None:
        ...

