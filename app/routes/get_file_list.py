"""
file_name = get_file_list.py
Created On: 2024/06/16
Lasted Updated: 2024/06/16
Description: _FILL OUT HERE_
Edit Log:
2024/06/16
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from sanic import Blueprint
from sanic.request import Request

# LOCAL LIBRARY IMPORTS

FILE_LIST_BLUEPRINT = Blueprint("file_list_blueprint", url_prefix="/")


@FILE_LIST_BLUEPRINT.post("/getFileList")
async def get_file_list(request: Request) -> None: ...
