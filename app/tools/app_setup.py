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

# THIRD PARTY LIBRARY IMPORTS
from sanic import Sanic

# from sanic.log import LOGGING_CONFIG_DEFAULTS

# LOCAL LIBRARY IMPORTS
from tools.middleware import Middleware
from tools.tasks import task_reload_vault
from routes.blueprints import BLUEPRINTS
from tools.vault import Vault


class App:
    def __init__(self) -> None:
        self._app = Sanic("ObsidianDocumentRetrieverSvc")
        self._register_middleware()
        self._register_blueprints()
        self._register_globals()
        self._register_tasks()

    # PROPERTIES START HERE

    @property
    def app(self) -> Sanic:
        return self._app

    # PROPERTIES END HERE

    # PUBLIC METHODS START HERE

    def run(self) -> None:
        self.app.run(host="0.0.0.0", port=8000)

    # PUBLIC METHODS END HERE

    # PRIVATE METHODS START HERE

    def _register_middleware(self) -> None:
        self.app.register_middleware(Middleware.request_middleware, "request")
        self.app.register_middleware(Middleware.response_middleware, "response")

    def _register_blueprints(self) -> None:
        for blueprint in BLUEPRINTS:
            self.app.blueprint(blueprint)

    def _register_globals(self) -> None:
        self.app.config["VAULT"] = Vault()

    def _register_tasks(self) -> None:
        self.app.add_task(task_reload_vault(self.app))

    # PRIVATE METHODS END HERE
