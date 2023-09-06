from __future__ import annotations
import asyncio
from core import Bot


async def main() -> None:
    # TODO
    async with Bot() as bot:
        await bot.start(token="", reconnect=True)


if __name__ == "__main__":
    asyncio.run(main())
