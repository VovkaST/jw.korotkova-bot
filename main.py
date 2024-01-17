import asyncio

from telebot import logger

import info
import settings
from bot import bot

logger.setLevel(settings.LOGGING_LEVEL)


if __name__ == "__main__":
    try:
        logger.info(f"Start polling (v.{info.__version__})")
        asyncio.run(bot.polling())
    except KeyboardInterrupt:
        logger.info("Stopped by user")
