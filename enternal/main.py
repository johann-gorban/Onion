import os
from collections.abc import Sequence

from fastapi import FastAPI

from config import Config
from handlers import setup_routers
from storages.engine import Engine

CONF_FILE = ".env"



config_path = os.path.join(os.path.dirname(__file__), CONF_FILE)
config = Config(config_path=config_path)
engine = Engine(config=config)
app = FastAPI(
    on_startup=engine.connect(),
    on_shutdown=...
)

setup_routers(app)
