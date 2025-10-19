import pytest
from app.core.role import Roles

# test user groups data
user_gid = "test_user_gid"
manager_gid = "test_manager_gid"
admin_gid = "test_admin_gid"
unknown_gid = "test_unknown_gid"


# fixture for setting environment variables using monkeypatch
@pytest.fixture(autouse=True)
def set_app_security_settings_env_fixture(monkeypatch):
    monkeypatch.setenv("SECURITY__USERS_GROUP_ID", user_gid)
    monkeypatch.setenv("SECURITY__MANAGERS_GROUP_ID", manager_gid)
    monkeypatch.setenv("SECURITY__ADMINS_GROUP_ID", admin_gid)


def test_get_user_roles_single():
    assert Roles.get_user_roles([user_gid]) == {"user"}
    assert Roles.get_user_roles([manager_gid]) == {"manager"}
    assert Roles.get_user_roles([admin_gid]) == {"admin"}


def test_get_user_roles_multiple():
    assert Roles.get_user_roles([user_gid, manager_gid]) == {"user", "manager"}
    assert Roles.get_user_roles([manager_gid, admin_gid]) == {"manager", "admin"}
    assert Roles.get_user_roles([user_gid, admin_gid]) == {"user", "admin"}
    assert Roles.get_user_roles([user_gid, manager_gid, admin_gid]) == {"user", "manager", "admin"}


def test_get_user_roles_empty():
    assert Roles.get_user_roles([]) == set()
    assert Roles.get_user_roles([unknown_gid]) == set()


def test_get_max_role_priority():
    # priority: user < manager < admin
    assert Roles.get_max_role([user_gid]) == "user"
    assert Roles.get_max_role([manager_gid]) == "manager"
    assert Roles.get_max_role([admin_gid]) == "admin"
    assert Roles.get_max_role([user_gid, manager_gid]) == "manager"
    assert Roles.get_max_role([user_gid, admin_gid]) == "admin"
    assert Roles.get_max_role([manager_gid, admin_gid]) == "admin"
    assert Roles.get_max_role([user_gid, manager_gid, admin_gid]) == "admin"


def test_get_max_role_empty():
    assert Roles.get_max_role([]) is None
    assert Roles.get_max_role([unknown_gid]) is None
