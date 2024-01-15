from telebot import logger, types
from telebot.async_telebot import AsyncTeleBot

import settings
from const import Buttons, Messages

bot = AsyncTeleBot(settings.TOKEN)
main_menu = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
main_menu.add(
    types.KeyboardButton(Buttons.HELP.value),
    types.KeyboardButton(Buttons.ABOUT.value),
)


@bot.message_handler(commands=["start"])
async def handler_start(message: types.Message):
    logger.info("Received start command [%s@%s]", message.from_user.id, message.from_user.username)
    await bot.send_message(message.chat.id, Messages.START.value, reply_markup=main_menu)


@bot.message_handler(content_types=["text"])
async def handler_messages(message: types.Message):
    logger.info("Received message: %s [%s@%s]", message.text, message.from_user.id, message.from_user.username)
    if message.text == Buttons.HELP:
        await bot.send_message(message.chat.id, Messages.HELP.value)
    elif message.text == Buttons.ABOUT:
        await bot.send_message(message.chat.id, Messages.ABOUT.value)
    else:
        logger.info("Unknown message: %s [%s@%s]", message.text, message.from_user.id, message.from_user.username)
        await bot.send_message(message.chat.id, Messages.UNKNOWN.value)
