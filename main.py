import asyncio

from telebot import logger

import settings
from bot import bot

logger.setLevel(settings.LOGGING_LEVEL)


if __name__ == "__main__":
    try:
        logger.info("Start polling")
        asyncio.run(bot.polling())
    except KeyboardInterrupt:
        logger.info("Stopped by user")
