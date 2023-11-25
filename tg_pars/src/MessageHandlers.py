from pyrogram.types import Message
from .setup.UserClient import Bot


async def register_message_handlers():
    # Handle binance messages
    @Bot.userbot.on_message(group=-1001146915409)
    async def handle_binance_listings(_, message: Message):
        if message.chat.id != -1001146915409:
            return
        text = message.text or message.caption
        if "Will List " in text:
            await Bot.userbot.forward_messages(
                -1001987280310,
                message.chat.id,
                message.id,
            )

    # Handle bybit messages
    @Bot.userbot.on_message(group=-1001449478440)
    async def handle_bybit_listings(_, message: Message):
        if message.chat.id != -1001449478440:
            return
        text = message.text or message.caption
        if "Now Live on Bybit Spot" in text or \
                "Perpetual Contract" in text:
            await Bot.userbot.forward_messages(
                -1001987280310,
                message.chat.id,
                message.id,
            )

    # Handle gate messages
    @Bot.userbot.on_message(group=-1001179920418)
    async def handle_gate_listings(_, message: Message):
        if message.chat.id != -1001179920418:
            return
        text = message.text or message.caption
        if "Новый листинг" in text:
            await Bot.userbot.forward_messages(
                -1001987280310,
                message.chat.id,
                message.id,
            )

    # Handle okex messages
    @Bot.userbot.on_message(group=-1001199213090)
    async def handle_okex_listings(_, message: Message):
        if message.chat.id != -1001199213090:
            return
        text = message.text or message.caption
        if "to list" in text:
            await Bot.userbot.forward_messages(
                -1001987280310,
                message.chat.id,
                message.id,
            )

    # Handle test messages
    @Bot.userbot.on_message(group=-1001987280310)
    async def handle_test_messages(_, message: Message):
        if message.chat.id != -1001987280310:
            return
        text = message.text or message.caption
        if "тест" in text:
            await Bot.userbot.forward_messages(
                -1001987280310,
                message.chat.id,
                message.id,
            )
