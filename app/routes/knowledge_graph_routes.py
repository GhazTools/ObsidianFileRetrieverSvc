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
from os.path import join
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
    KNOWLEDGE_GRAPH_BLUEPRINT,
    resources={r"/api/*": {"origins": "*"}},
    methods=["GET"],
    allow_headers=["Content-Type", "Authorization"],
    supports_credentials=True,
)


@KNOWLEDGE_GRAPH_BLUEPRINT.get("/")
async def handle_get_knowledge_graph(request):
    # Accessing a single query parameter (e.g., 'query')
    vault_name = request.args.get(
        "vaultName", cast(str, getenv("DEFAULT_OBSIDIAN_VAULT"))
    )  # Returns the first value for 'query' or None if not present

    json_path = join(getenv("DATA_DIRECTORY_PATH"), f"{vault_name}.json")

    vault_data: dict = {}

    with open(json_path, "r", encoding="UTF_8") as json_file:
        vault_data = load(json_file)

    return JSONResponse(vault_data)
