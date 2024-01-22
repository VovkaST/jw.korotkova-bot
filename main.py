import asyncio
from time import sleep

from telebot import logger
from telebot.asyncio_helper import RequestTimeout

import info
import settings
from bot import bot
from utils import init_bot

logger.setLevel(settings.LOGGING_LEVEL)


def main():
    async def _main():
        await init_bot(bot)
        await bot.polling()

    while True:
        try:
            logger.info(f"Start polling (v.{info.__version__})")
            asyncio.run(_main())
        except RequestTimeout as error:
            logger.error(f"RequestTimeout occurred: {error}")
            logger.info(f"Sleep {settings.RESTART_TIMEOUT} sec and restarting...")
            sleep(settings.RESTART_TIMEOUT)
        except KeyboardInterrupt:
            logger.info("Stopped by user")
            break
        except Exception as error:
            logger.info(f"Unhandled error occurred: {error}. Stop polling.")
            break


if __name__ == "__main__":
    main()
