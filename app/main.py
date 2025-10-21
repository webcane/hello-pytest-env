from app.core.config import get_app_settings
import sys


app_settings = get_app_settings()

# validate that app_name is set and not empty
if not app_settings.app_name or not app_settings.app_name.strip():
    print("Error: 'app_name' not set in .env or is empty.")
    sys.exit(1)

print(f"app_name: {app_settings.app_name}")
