import logging
from pyrogram import Client
from os import environ


# Singleton for storing the session
class Bot:
    userbot: None | Client = None


def create_connection() -> bool:
    api_id: str | None = environ.get("TELEGRAM_API_PUBLIC_ID")
    api_hash: str | None = environ.get("TELEGRAM_API_SECRET_HASH")

    if api_id and api_hash and Bot.userbot is None:
        c = Client("Manageable_Account", api_id, api_hash)
        Bot.userbot = c
        return True

    logging.critical("Could not get dotenv variable")
    return False
