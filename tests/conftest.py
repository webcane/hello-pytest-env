import pytest


# fixture for setting environment variables using monkeypatch
@pytest.fixture(autouse=True)
def set_app_settings_env_fixture(monkeypatch):
    monkeypatch.setenv("APP_NAME", "test_app")



