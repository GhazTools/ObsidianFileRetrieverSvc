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
from sanic.response import text, HTTPResponse
from sanic.log import logger
from pydantic import ValidationError

# LOCAL LIBRARY IMPORTS
from models.model import BaseRequest


class Middleware:
    @staticmethod
    async def request_middleware(request: Request) -> None | HTTPResponse:
        logger.info("request received %s", request.path)

        if request.method == "POST":
            print("REAHCED HERE")
            token_granter = request.app.config["TOKEN_GRANTER"]
            try:
                # Parse request body into Pydantic model
                user_token = BaseRequest(**request.json)

                # If needed, use user_token.user and user_token.token for further processing
                is_valid: bool = token_granter.validate_token(
                    user_token.user, user_token.token
                )

                if not is_valid:
                    raise ValueError("Inavlid token")

            except ValidationError as e:
                print("Invalid error", e)
                return text("Unsupported endpoint.")
            except ValueError as e:
                print("Invalid token", e)
                return text("Unsupported endpoint.")

        print(request, request.path)
        return None

    @staticmethod
    async def response_middleware(
        request: Request,
        response: Any,
    ) -> None:
        print(request, response)
        print("success")

    # PRIVATE METHODS HERE
