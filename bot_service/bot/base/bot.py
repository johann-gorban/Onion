import logging

from aiogram import Bot

from bot.base.defaults import DEFAULTS, Defaults
from bot.base.dispatcher import create_dispatcher, setup_routers
from bot.config import Config
from bot.logger import BOT_LOGGER, setup_logging
from bot.routers import routers

__all__ = (
    "ITSBot",
    "run_bot",
)


class ITSBot(Bot):
    def __init__(self, token: str, defaults: Defaults):
        super().__init__(token=token, default=defaults)
        self.logger = logging.getLogger(BOT_LOGGER)


async def run_bot(config_path: str) -> ITSBot:
    setup_logging()

    config = Config(config_path)
    bot = ITSBot(token=config.token, defaults=DEFAULTS)
    dp = create_dispatcher()

    setup_routers(dp, routers)

    bot.logger.info("Starting bot...")
    # await bot.delete_webhook(drop_pending_updates=True)  # TODO??
    await dp.start_polling(bot)
