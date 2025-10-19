from dotenv import load_dotenv

load_dotenv()
from app.core.config import get_app_settings
import sys

settings = get_app_settings()

# validate that app_name is set and not empty
if not settings.app_name or not settings.app_name.strip():
    print("Ошибка: app_name не задан или пустой в конфиге.")
    sys.exit(1)

print(f"app_name: {settings.app_name}")
