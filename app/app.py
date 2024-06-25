"""
file_name = app.py
Created On: 2024/06/16
Lasted Updated: 2024/06/16
Description: _FILL OUT HERE_
Edit Log:
2024/06/16
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from tools.app_setup import AppSetup

APP_SETUP: AppSetup = AppSetup()
app = APP_SETUP.app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)