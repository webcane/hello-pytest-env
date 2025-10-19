from dataclasses import dataclass
from typing import List, Set, Optional

from app.core.config import get_app_settings


@dataclass(frozen=True)
class _Role:
    name: str
    order: int

    @property
    def group_id(self) -> str:
        settings = get_app_settings()
        if self.name == "user":
            return settings.security.users_group_id
        elif self.name == "manager":
            return settings.security.managers_group_id
        elif self.name == "admin":
            return settings.security.admins_group_id
        else:
            raise ValueError(f"Unknown role: {self.name}")


class Roles:
    @staticmethod
    def _get_all_roles() -> List["_Role"]:
        """Return a list of all roles (name and order). Order: user < manager < admin."""
        return [_Role("user", 0), _Role("manager", 1), _Role("admin", 2)]

    @classmethod
    def get_max_role(cls, ids: List[str]) -> Optional[str]:
        """Return the highest priority role name for the given group IDs (by order)."""
        roles = [role for role in cls._get_all_roles() if role.group_id in ids]
        if not roles:
            return None
        max_role = max(roles, key=lambda role: role.order)
        return max_role.name

    @classmethod
    def get_user_roles(cls, ids: List[str]) -> Set[str]:
        """Return a set of role names for the given group IDs."""
        return {role.name for role in cls._get_all_roles() if role.group_id in ids}
