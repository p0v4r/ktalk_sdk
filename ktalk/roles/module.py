"""Roles module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class RolesModule:
    """Module for managing roles in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_roles_sync(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список ролей.
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = self._client.get("/api/roles", params=params)
        response.raise_for_status()
        return response.json()

    async def get_roles_async(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список ролей (async).
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = await self._client.get("/api/roles", params=params)
        response.raise_for_status()
        return response.json()

    def get_role_by_id_sync(self, role_id: str) -> Any:
        """
        Получить информацию о роли по ID.
        """
        response = self._client.get(f"/api/roles/{role_id}")
        response.raise_for_status()
        return response.json()

    async def get_role_by_id_async(self, role_id: str) -> Any:
        """
        Получить информацию о роли по ID (async).
        """
        response = await self._client.get(f"/api/roles/{role_id}")
        response.raise_for_status()
        return response.json()

    def create_role_sync(self, role_data: dict) -> Any:
        """
        Создать новую роль.
        """
        response = self._client.post("/api/roles", json=role_data)
        response.raise_for_status()
        return response.json()

    async def create_role_async(self, role_data: dict) -> Any:
        """
        Создать новую роль (async).
        """
        response = await self._client.post("/api/roles", json=role_data)
        response.raise_for_status()
        return response.json()

    def update_role_sync(self, role_id: str, role_data: dict) -> Any:
        """
        Изменить настройки роли.
        """
        response = self._client.put(f"/api/roles/{role_id}", json=role_data)
        response.raise_for_status()
        return response.json()

    async def update_role_async(self, role_id: str, role_data: dict) -> Any:
        """
        Изменить настройки роли (async).
        """
        response = await self._client.put(f"/api/roles/{role_id}", json=role_data)
        response.raise_for_status()
        return response.json()

    def delete_role_sync(self, role_id: str) -> Any:
        """
        Удалить роль.
        """
        response = self._client.delete(f"/api/roles/{role_id}")
        response.raise_for_status()
        return response.json()

    async def delete_role_async(self, role_id: str) -> Any:
        """
        Удалить роль (async).
        """
        response = await self._client.delete(f"/api/roles/{role_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_roles(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_roles_async(*args, **kwargs)
        else:
            return self.get_roles_sync(*args, **kwargs)

    def get_role_by_id(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_role_by_id_async(*args, **kwargs)
        else:
            return self.get_role_by_id_sync(*args, **kwargs)

    def create_role(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_role_async(*args, **kwargs)
        else:
            return self.create_role_sync(*args, **kwargs)

    def update_role(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_role_async(*args, **kwargs)
        else:
            return self.update_role_sync(*args, **kwargs)

    def delete_role(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_role_async(*args, **kwargs)
        else:
            return self.delete_role_sync(*args, **kwargs)