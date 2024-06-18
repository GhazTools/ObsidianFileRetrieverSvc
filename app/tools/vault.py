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

# THIRD PARTY LIBRARY IMPORTS
from obsidian_wrapper.obsidian_vault import ObsidianVault

# LOCAL LIBRARY IMPORTS


class Vault:
    def __init__(self) -> None:
        self._vault = ObsidianVault(
            "/Users/ghaz/documents/Obsidian Vaults/Ghazs Knowledge Vault"
        )
        # self._vault = ObsidianVault(getenv("PATH_TO_OBSIDIAN_VAULT"))

    def reload_vault(self) -> None:
        try:
            self._vault.reload_vault()
        except ValueError as e:
            print(f"Unable to convert Error: {e}")
