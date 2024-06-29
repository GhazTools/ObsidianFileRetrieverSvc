"""
file_name = blueprints.py
Created On: 2024/06/16
Lasted Updated: 2024/06/16
Description: _FILL OUT HERE_
Edit Log:
2024/06/16
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import List

# THIRD PARTY LIBRARY IMPORTS
from sanic import Blueprint
from sanic.request import Request
from sanic.response import text, HTTPResponse

# LOCAL LIBRARY IMPORTS
from routes.obsidian_routes import OBSIDIAN_ROUTES_BLUEPRINT
from routes.knowledge_graph_routes import KNOWLEDGE_GRAPH_BLUEPRINT


ENTRY_POINT_BLUEPRINT = Blueprint("entry_point_blueprint", url_prefix="/")


@ENTRY_POINT_BLUEPRINT.get("/")
async def entry_point(request: Request) -> HTTPResponse:
    return text("App is currently running.")


BLUEPRINTS: List[Blueprint] = [
    ENTRY_POINT_BLUEPRINT,
    OBSIDIAN_ROUTES_BLUEPRINT,
    KNOWLEDGE_GRAPH_BLUEPRINT,
]
