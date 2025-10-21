from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SecuritySettings(BaseSettings):
    users_group_id: str = Field(description="'users' security group id")
    managers_group_id: str = Field(description="'managers' security group id")
    admins_group_id: str = Field(description="'administrators' security group id")

    def get_all_group(self) -> list[str]:
        """Return all security group IDs as a list."""
        return [self.users_group_id, self.managers_group_id, self.admins_group_id]


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = Field(validation_alias="APP_NAME")
    debug: bool = False
    security: SecuritySettings


# def get_app_settings():
#     """Return a singleton instance of AppSettings for production use."""
#     return _singleton_app_settings()
#
#
# # Use LRU cache to ensure singleton behavior
# @lru_cache(maxsize=1)
# def _singleton_app_settings():
#     return AppSettings()


# def reset_app_settings_cache():
#     """Reset the singleton AppSettings cache (for testing)."""
#     _singleton_app_settings.cache_clear()

app_settings = AppSettings()
