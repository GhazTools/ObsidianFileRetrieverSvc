"""
file_name = vault.py
Created On: 2024/06/18
Lasted Updated: 2024/06/18
Description: _FILL OUT HERE_
Edit Log:
2024/06/18
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from os import getenv
from typing import Any, List, Dict, Tuple, TypedDict

# THIRD PARTY LIBRARY IMPORTS
from obsidian_wrapper.obsidian_vault import (
    ObsidianVault,
    ObsidianMarkdownFile,
    VaultTree,
)

# LOCAL LIBRARY IMPORTS


class FolderData(TypedDict):
    folderName: str
    contents: List[Dict[str, str]]


class Vault:
    def __init__(self) -> None:
        self._vault = ObsidianVault(getenv("OBSIDIAN_DIRECTORY_PATH"))

    def reload_vault(self) -> None:
        try:
            self._vault.reload_vault()
        except ValueError as e:
            self._vault = ObsidianVault(getenv("OBSIDIAN_DIRECTORY_PATH"))
            print(f"Unable to convert Error: {e}, reset vault")

    def get_vault_files(self) -> List[str]:
        markdown_files: Dict[str, ObsidianMarkdownFile] = self._vault.markdown_files

        return list(markdown_files.keys())

    def get_vault_file_contents_by_name(self, file_name: str) -> str:
        markdown_files: Dict[str, ObsidianMarkdownFile] = self._vault.markdown_files

        if not file_name in markdown_files:
            raise KeyError(f"File was not found in obsidian vault ${file_name}")

        markdown_file: ObsidianMarkdownFile = markdown_files[file_name]
        contents: str = ""

        with open(markdown_file.file_path, "r", encoding="UTF-8") as current_file:
            for line in current_file:
                contents += line

        return contents

    def get_file_contents_by_name_detailed(self, file_name: str) -> Any:
        markdown_files: Dict[str, ObsidianMarkdownFile] = self._vault.markdown_files

        if not file_name in markdown_files:
            raise KeyError("File was not found in obsidian vault")

        markdown_file: ObsidianMarkdownFile = markdown_files[file_name]

        return markdown_file.get_file_contents(as_dict=True)

    def get_folder_contents(self, folder_name: str) -> FolderData:
        data: Tuple[str, VaultTree, int] = self._vault.get_folder(
            folder_path=folder_name
        )

        # Contents are only only one level down
        current_folder: FolderData = {
            "folderName": data[0],
            "contents": [],
            # "size": data[2]
        }

        for object_name, value in data[1].items():
            content_type: str = ""

            if isinstance(value, dict):
                content_type = "Folder"
            else:
                content_type = "File"

            current_folder["contents"].append(
                {"objectName": object_name, "contentType": content_type}
            )

        current_folder["contents"] = sorted(
            current_folder["contents"], key=lambda d: d["objectName"]
        )

        return current_folder
