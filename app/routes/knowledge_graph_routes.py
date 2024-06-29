"""
file_name = knowledge_graph_routes.py
Created On: 2024/06/26
Lasted Updated: 2024/06/26
Description: _FILL OUT HERE_
Edit Log:
2024/06/26
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from os import getenv
from os.path import join, exists
from typing import cast
from json import load

# THIRD PARTY LIBRARY IMPORTS
from sanic import Blueprint
from sanic.response import json as JSONResponse
from sanic_cors import CORS

# LOCAL LIBRARY IMPORTS


KNOWLEDGE_GRAPH_BLUEPRINT = Blueprint(
    "knowledge_graph_blueprint", url_prefix="/knowledgeGraph/"
)
CORS(
    KNOWLEDGE_GRAPH_BLUEPRINT
)


@KNOWLEDGE_GRAPH_BLUEPRINT.get("/")
async def handle_get_knowledge_graph(request):
    # Accessing a single query parameter (e.g., 'query')
    default_vault_name: str = cast(str, getenv("DEFAULT_OBSIDIAN_VAULT"))
    
    vault_name = request.args.get(
        "vaultName", default_vault_name
    )  

    json_path = join(getenv("DATA_DIRECTORY_PATH"), f"{vault_name}.json")
    
    if not exists(json_path):
        json_path = join(getenv("DATA_DIRECTORY_PATH"), f"{default_vault_name}.json")

    vault_data: dict = {}

    with open(json_path, "r", encoding="UTF_8") as json_file:
        vault_data = load(json_file)

    return JSONResponse(vault_data)
