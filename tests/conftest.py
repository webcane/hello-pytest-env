import pytest
from app.core.config import reset_app_settings_cache


# fixture to reset the cached app settings before each test
# it garantees that changes to environment variables are reflected in app settings
@pytest.fixture(autouse=True)
def reset_app_settings_cache_fixture():
    reset_app_settings_cache()


# fixture for setting environment variables using monkeypatch
@pytest.fixture(autouse=True)
def set_app_settings_env_fixture(monkeypatch):
    monkeypatch.setenv("APP_NAME", "test_app")



