import logging
import pathlib

import environ

ROOT_PATH = pathlib.Path(__file__).parent

env = environ.Env()
env.read_env(ROOT_PATH / ".env")

TOKEN = env.str("TOKEN")
LOGGING_LEVEL = env.int("LOGGING_LEVEL", logging.INFO)
RESTART_TIMEOUT = env.int("RESTART_TIMEOUT", 5)
