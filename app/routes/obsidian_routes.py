"""
file_name = obsidian_routes.py
Created On: 2024/06/24
Lasted Updated: 2024/06/24
Description: _FILL OUT HERE_
Edit Log:
2024/06/24
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json, HTTPResponse

# LOCAL LIBRARY IMPORTS
from tools.vault import Vault


OBSIDIAN_ROUTES_BLUEPRINT = Blueprint("obsidian_routes_blueprint", url_prefix="/")


@OBSIDIAN_ROUTES_BLUEPRINT.post("/getFileList")
def get_file_list(request: Request) -> HTTPResponse:
    vault: Vault = request.app.config["VAULT"]

    return json({"file_names": sorted(vault.get_vault_files())})


@OBSIDIAN_ROUTES_BLUEPRINT.post("/getFileContents")
def get_file_contents(request: Request) -> HTTPResponse:
    vault: Vault = request.app.config["VAULT"]
    file_name = request.json.get("fileName")  # Returns the first value for 'filename'

    return json({"file_contents": vault.get_vault_file_contents_by_name(file_name)})


@OBSIDIAN_ROUTES_BLUEPRINT.post("/getFileContentsDetailed")
def get_file_contents_detailed(request: Request) -> HTTPResponse:
    vault: Vault = request.app.config["VAULT"]
    file_name = request.json.get("fileName")  # Returns the first value for 'filename'

    return json({"file_contents": vault.get_file_contents_by_name_detailed(file_name)})


@OBSIDIAN_ROUTES_BLUEPRINT.post("/getFolderContents")
def get_folder_contents(request: Request) -> HTTPResponse:
    vault: Vault = request.app.config["VAULT"]
    folder_name = request.json.get("folderName")

    return json(vault.get_folder_contents(folder_name))
