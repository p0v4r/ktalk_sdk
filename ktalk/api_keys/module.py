"""API Keys module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class ApplicationsModule:
    """Module for managing API keys (applications) in KTalk."""
    
    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_applications_sync(self, top: int = 50, start: str = None) -> Any:
        """Получить информацию об API-ключах."""
        params = {"top": top}
        if start:
            params["start"] = start
            
        response = self._client.get("/api/domain/applications", params=params)
        response.raise_for_status()
        return response.json()

    async def get_applications_async(self, top: int = 50, start: str = None) -> Any:
        """Получить информацию об API-ключах (async)."""
        params = {"top": top}
        if start:
            params["start"] = start
            
        response = await self._client.get("/api/domain/applications", params=params)
        response.raise_for_status()
        return response.json()

    def get_access_info_sync(self) -> Any:
        """Получить информацию о правах текущего API-ключа."""
        response = self._client.get("/api/domain/applications/access-info")
        response.raise_for_status()
        return response.json()

    async def get_access_info_async(self) -> Any:
        """Получить информацию о правах текущего API-ключа (async)."""
        response = await self._client.get("/api/domain/applications/access-info")
        response.raise_for_status()
        return response.json()

    def create_application_sync(self, application_data: dict) -> Any:
        """Создать новый API-ключ."""
        response = self._client.post("/api/domain/applications", json=application_data)
        response.raise_for_status()
        return response.json()

    async def create_application_async(self, application_data: dict) -> Any:
        """Создать новый API-ключ (async)."""
        response = await self._client.post("/api/domain/applications", json=application_data)
        response.raise_for_status()
        return response.json()

    def update_application_sync(self, application_key: str, application_data: dict) -> Any:
        """Изменить настройки API-ключа."""
        response = self._client.put(f"/api/domain/applications/{application_key}", json=application_data)
        response.raise_for_status()
        return response.json()

    async def update_application_async(self, application_key: str, application_data: dict) -> Any:
        """Изменить настройки API-ключа (async)."""
        response = await self._client.put(f"/api/domain/applications/{application_key}", json=application_data)
        response.raise_for_status()
        return response.json()

    def delete_application_sync(self, application_key: str) -> Any:
        """Удалить API-ключ."""
        response = self._client.delete(f"/api/domain/applications/{application_key}")
        response.raise_for_status()
        return response.json()

    async def delete_application_async(self, application_key: str) -> Any:
        """Удалить API-ключ (async)."""
        response = await self._client.delete(f"/api/domain/applications/{application_key}")
        response.raise_for_status()
        return response.json()

    def refresh_token_sync(self, application_key: str) -> Any:
        """Продлить время жизни API-ключа."""
        response = self._client.post(f"/api/domain/applications/{application_key}/refresh-token")
        response.raise_for_status()
        return response.json()

    async def refresh_token_async(self, application_key: str) -> Any:
        """Продлить время жизни API-ключа (async)."""
        response = await self._client.post(f"/api/domain/applications/{application_key}/refresh-token")
        response.raise_for_status()
        return response.json()

    def recreate_token_sync(self, application_key: str) -> Any:
        """Перевыпустить API-ключ."""
        response = self._client.post(f"/api/domain/applications/{application_key}/recreate-token")
        response.raise_for_status()
        return response.json()

    async def recreate_token_async(self, application_key: str) -> Any:
        """Перевыпустить API-ключ (async)."""
        response = await self._client.post(f"/api/domain/applications/{application_key}/recreate-token")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_applications(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_applications_async(*args, **kwargs)
        else:
            return self.get_applications_sync(*args, **kwargs)

    def get_access_info(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_access_info_async(*args, **kwargs)
        else:
            return self.get_access_info_sync(*args, **kwargs)

    def create_application(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_application_async(*args, **kwargs)
        else:
            return self.create_application_sync(*args, **kwargs)

    def update_application(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_application_async(*args, **kwargs)
        else:
            return self.update_application_sync(*args, **kwargs)

    def delete_application(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_application_async(*args, **kwargs)
        else:
            return self.delete_application_sync(*args, **kwargs)

    def refresh_token(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.refresh_token_async(*args, **kwargs)
        else:
            return self.refresh_token_sync(*args, **kwargs)

    def recreate_token(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.recreate_token_async(*args, **kwargs)
        else:
            return self.recreate_token_sync(*args, **kwargs)