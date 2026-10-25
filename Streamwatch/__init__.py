from redbot.core.bot import Red

from .streamwatch import StreamWatch


async def setup(bot: Red) -> None:
    await bot.add_cog(StreamWatch(bot))
