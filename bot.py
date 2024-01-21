from telebot import logger, types
from telebot.async_telebot import AsyncTeleBot

import info
import settings
from const import Buttons, Commands, Messages

bot = AsyncTeleBot(settings.TOKEN)
inlines = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
inlines.add(
    types.KeyboardButton(Buttons.ORDER.value),
    types.KeyboardButton(Buttons.PRICE.value),
    types.KeyboardButton(Buttons.DELIVERY.value),
    types.KeyboardButton(Buttons.CARE.value),
    types.KeyboardButton(Buttons.ABOUT.value),
)


@bot.message_handler(commands=["start", Commands.RESTART.name.lower()])
async def handler_start(message: types.Message):
    logger.info("Received %s command [%s@%s]", message.text, message.from_user.id, message.from_user.username)
    await bot.send_message(message.chat.id, Messages.START.value, reply_markup=inlines)


@bot.message_handler(commands=[Commands.VERSION.name.lower()])
async def handler_version(message: types.Message):
    logger.info("Received %s command [%s@%s]", message.text, message.from_user.id, message.from_user.username)
    await bot.send_message(message.chat.id, Messages.VERSION.value % info.__version__, reply_markup=inlines)


@bot.message_handler(content_types=["text"])
async def handler_messages(message: types.Message):
    logger.info("Received message: %s [%s@%s]", message.text, message.from_user.id, message.from_user.username)
    if message.text == Buttons.ORDER:
        await bot.reply_to(message, Messages.ORDER.value)
    elif message.text == Buttons.PRICE:
        await bot.reply_to(message, Messages.PRICE.value)
    elif message.text == Buttons.DELIVERY:
        await bot.reply_to(message, Messages.DELIVERY.value)
    elif message.text == Buttons.CARE:
        await bot.reply_to(message, Messages.CARE.value)
    elif message.text == Buttons.ABOUT:
        await bot.reply_to(message, Messages.ABOUT.value)
    else:
        logger.info("Unknown message: %s [%s@%s]", message.text, message.from_user.id, message.from_user.username)
        await bot.reply_to(message, Messages.UNKNOWN.value)
