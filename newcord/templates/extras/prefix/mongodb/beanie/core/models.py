from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Sequence, Type, Union

from beanie import Document

if TYPE_CHECKING:
    from beanie import View

__all__: Sequence[str] = ("models",)

# Documentation: http://beanie-odm.dev/


# Create your models here.

# This will be used when we initialize beanie.
models: Optional[List[Union[Type[Document], Type[View], str]]] = []
