"""
file_name = middleware.py
Created On: 2024/06/16
Lasted Updated: 2024/06/16
Description: _FILL OUT HERE_
Edit Log:
2024/06/16
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import Any

# THIRD PARTY LIBRARY IMPORTS
from sanic.request import Request
from sanic.log import logger

# LOCAL LIBRARY IMPORTS


class Middleware:
    @staticmethod
    async def request_middleware(request: Request) -> None:
        logger.info("request received %s", request.path)

        print(request, request.path)

    @staticmethod
    async def response_middleware(request: Request, response: Any) -> None:
        print(request, response)
        print("success")

    # PRIVATE METHODS HERE
