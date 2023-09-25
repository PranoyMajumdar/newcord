from __future__ import annotations

from typing import Sequence
from questionary import Style

__all__: Sequence[str] = ("style",)


# fmt: off
style = Style([
    ('qmark', 'fg:#00ffff bold'),       # token in front of the question
    ('question', 'white bold'),               # question text
    ('answer', 'fg:black'),      # submitted answer text behind the question
    ('pointer', 'fg:#00ffff bold'),     # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#00ffff bold'), # pointed-at choice in select and checkbox prompts
    ('selected', 'fg:#cc5454'),         # style for a selected item of a checkbox
    ('separator', 'fg:#cc5454'),        # separator in lists
    ('instruction', ''),                # user instructions for select, rawselect, checkbox
    ('text', ''),                       # plain text
    ('disabled', 'fg:#858585 italic')   # disabled choices for select and checkbox prompts
])
