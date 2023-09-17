from __future__ import annotations

from typing import TYPE_CHECKING, Sequence, Optional, Union, ClassVar
from discord import ui

if TYPE_CHECKING:
    from discord import Interaction, Message, WebhookMessage, User, Member

__all__: Sequence[str] = ("View",)


class View(ui.View):
    message: ClassVar[Union[Message, WebhookMessage]]

    def __init__(
        self,
        *,
        timeout: Optional[float] = 180,
        author: Optional[Union[User, Member]],
    ):
        super().__init__(timeout=timeout)
        self.author = author

    async def interaction_check(self, interaction: Interaction, /) -> bool:
        if self.author and self.author.id != interaction.user.id:
            await interaction.response.send_message(
                f"This view can only be controlled by {self.author.mention}",
                ephemeral=True,
            )
            return False
        return True
