import asyncio

from telebot import logger

import info
import settings
from bot import bot
from utils import init_bot

logger.setLevel(settings.LOGGING_LEVEL)


def main():
    async def _main():
        await init_bot(bot)
        await bot.polling()

    try:
        logger.info(f"Start polling (v.{info.__version__})")
        asyncio.run(_main())
    except KeyboardInterrupt:
        logger.info("Stopped by user")


if __name__ == "__main__":
    main()
