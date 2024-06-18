"""
file_name = tasks.py
Created On: 2024/06/18
Lasted Updated: 2024/06/18
Description: _FILL OUT HERE_
Edit Log:
2024/06/18
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from asyncio import sleep
from typing import cast

# THIRD PARTY LIBRARY IMPORTS
from sanic import Sanic

# LOCAL LIBRARY IMPORTS
from tools.vault import Vault


async def task_reload_vault(app: Sanic) -> None:
    await sleep(3600)  # Task is run every hour
    cast(Vault, app.config["VAULT"]).reload_vault()
