from logging import getLogger

from aiogram import Dispatcher, Router

from bot.logger import DP_LOGGER


def create_dispatcher() -> Dispatcher:
    return Dispatcher()  # TODO: добавить всякие параметры


def setup_routers(dp: Dispatcher, routers: list[Router]) -> None:
    logger = getLogger(DP_LOGGER)

    dp.include_routers(*routers)
    logger.info(
        "Included routers: [%s]", ", ".join(router.name for router in routers)
    )
