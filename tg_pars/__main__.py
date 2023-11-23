import logging

from dotenv import load_dotenv
from src.setup.EnvValidation import EnvValidation
from src.setup.UserClient import create_connection
from src.MessageHandlers import register_message_handlers
from src.setup.UserClient import Bot


def initial_setup():
    """Start the app"""
    load_dotenv()
    EnvValidation()

    connection_creation_result = create_connection()
    if connection_creation_result:
        logging.info("Connection with userbot established")
    else:
        logging.critical("Failed to establish connection")
        raise ConnectionError("Failed to establish connection")


async def main():
    await register_message_handlers()

    logging.warning("Started the userbot")


if __name__ == "__main__":
    initial_setup()
    try:
        Bot.userbot.run(main())
        Bot.userbot.run()
    except KeyboardInterrupt:
        logging.critical("Finished")
