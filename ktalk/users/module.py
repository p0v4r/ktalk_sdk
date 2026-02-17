"""Users module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class UsersModule:
    """Module for managing users in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_users_sync(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список пользователей.
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = self._client.get("/api/users", params=params)
        response.raise_for_status()
        return response.json()

    async def get_users_async(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список пользователей (async).
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = await self._client.get("/api/users", params=params)
        response.raise_for_status()
        return response.json()

    def get_user_by_key_sync(self, user_key: str) -> Any:
        """
        Получить информацию о пользователе по ключу.
        """
        response = self._client.get(f"/api/users/{user_key}")
        response.raise_for_status()
        return response.json()

    async def get_user_by_key_async(self, user_key: str) -> Any:
        """
        Получить информацию о пользователе по ключу (async).
        """
        response = await self._client.get(f"/api/users/{user_key}")
        response.raise_for_status()
        return response.json()

    def create_user_sync(self, user_data: dict) -> Any:
        """
        Создать нового пользователя.
        """
        response = self._client.post("/api/users", json=user_data)
        response.raise_for_status()
        return response.json()

    async def create_user_async(self, user_data: dict) -> Any:
        """
        Создать нового пользователя (async).
        """
        response = await self._client.post("/api/users", json=user_data)
        response.raise_for_status()
        return response.json()

    def update_user_sync(self, user_key: str, user_data: dict) -> Any:
        """
        Изменить настройки пользователя.
        """
        response = self._client.put(f"/api/users/{user_key}", json=user_data)
        response.raise_for_status()
        return response.json()

    async def update_user_async(self, user_key: str, user_data: dict) -> Any:
        """
        Изменить настройки пользователя (async).
        """
        response = await self._client.put(f"/api/users/{user_key}", json=user_data)
        response.raise_for_status()
        return response.json()

    def delete_user_sync(self, user_key: str) -> Any:
        """
        Удалить пользователя.
        """
        response = self._client.delete(f"/api/users/{user_key}")
        response.raise_for_status()
        return response.json()

    async def delete_user_async(self, user_key: str) -> Any:
        """
        Удалить пользователя (async).
        """
        response = await self._client.delete(f"/api/users/{user_key}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_users(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_users_async(*args, **kwargs)
        else:
            return self.get_users_sync(*args, **kwargs)

    def get_user_by_key(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_user_by_key_async(*args, **kwargs)
        else:
            return self.get_user_by_key_sync(*args, **kwargs)

    def create_user(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_user_async(*args, **kwargs)
        else:
            return self.create_user_sync(*args, **kwargs)

    def update_user(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_user_async(*args, **kwargs)
        else:
            return self.update_user_sync(*args, **kwargs)

    def delete_user(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_user_async(*args, **kwargs)
        else:
            return self.delete_user_sync(*args, **kwargs)