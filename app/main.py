from app.core.config import app_settings
import sys


# validate that app_name is set and not empty
if not app_settings.app_name or not app_settings.app_name.strip():
    print("Ошибка: app_name не задан или пустой в конфиге.")
    sys.exit(1)

print(f"app_name: {app_settings.app_name}")
