"""
file_name = app_setup.py
Created On: 2024/06/16
Lasted Updated: 2024/06/16
Description: _FILL OUT HERE_
Edit Log:
2024/06/16
    - Created file
"""

# STANDARD LIBRARY IMPORTS
# from logging import CRITICAL, DEBUG, ERROR, INFO, NOTSET, WARNING, Formatter, Logger
# from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from os import getenv

# THIRD PARTY LIBRARY IMPORTS
from sanic import Sanic
from dotenv import load_dotenv
from token_granter_wrapper import token_granter_bindings

# from sanic.log import LOGGING_CONFIG_DEFAULTS

# LOCAL LIBRARY IMPORTS
from tools.middleware import Middleware
from tools.tasks import task_reload_vault
from tools.vault import Vault
from routes.blueprints import BLUEPRINTS


class AppSetup:
    def __init__(self) -> None:
        self.__load_dotenv()
        self._app = Sanic("ObsidianDocumentRetrieverSvc")

        # Register objects
        self._register_globals()
        self._register_middleware()
        self._register_blueprints()
        self._register_tasks()

    # PROPERTIES START HERE

    @property
    def app(self) -> Sanic:
        return self._app

    # PROPERTIES END HERE

    # PUBLIC METHODS START HERE
    # PUBLIC METHODS END HERE

    # PRIVATE METHODS START HERE

    def __load_dotenv(self) -> None:
        root_path = Path(__file__).resolve().parents[2]
        env_path = root_path / ".env"

        # Alternative way to get root path

        # file_path = abspath(file)
        # file_dir = dirname(file_path)
        # root_path = dirname(dirname(file_dir))
        # load_dotenv(dotenv_path=root_path)

        load_dotenv(dotenv_path=env_path)

    def _register_middleware(self) -> None:
        self.app.register_middleware(Middleware.request_middleware, "request")
        self.app.register_middleware(Middleware.response_middleware, "response")

    def _register_blueprints(self) -> None:
        for blueprint in BLUEPRINTS:
            self.app.blueprint(blueprint)

    def _register_globals(self) -> None:
        self.app.config["VAULT"] = Vault()
        self.app.config["TOKEN_GRANTER"] = token_granter_bindings.TokenGranter(
            getenv("TOKEN_GRANTER_URL")
        )

    def _register_tasks(self) -> None:
        self.app.add_task(task_reload_vault(self.app))

    # PRIVATE METHODS END HERE
