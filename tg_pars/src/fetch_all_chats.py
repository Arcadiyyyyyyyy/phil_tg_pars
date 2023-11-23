from .setup.UserClient import Bot


async def fetch_all_chats():
    async with Bot.userbot:
        async for chat in Bot.userbot.get_dialogs():
            print(chat.chat.id, chat.chat.title, sep="   |   ")
