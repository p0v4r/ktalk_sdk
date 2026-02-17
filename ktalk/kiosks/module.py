"""Kiosks module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class KiosksModule:
    """Module for managing kiosks in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_kiosks_sync(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список киосков.
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = self._client.get("/api/kiosks", params=params)
        response.raise_for_status()
        return response.json()

    async def get_kiosks_async(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список киосков (async).
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = await self._client.get("/api/kiosks", params=params)
        response.raise_for_status()
        return response.json()

    def get_kiosk_by_id_sync(self, kiosk_id: str) -> Any:
        """
        Получить информацию о киоске по ID.
        """
        response = self._client.get(f"/api/kiosks/{kiosk_id}")
        response.raise_for_status()
        return response.json()

    async def get_kiosk_by_id_async(self, kiosk_id: str) -> Any:
        """
        Получить информацию о киоске по ID (async).
        """
        response = await self._client.get(f"/api/kiosks/{kiosk_id}")
        response.raise_for_status()
        return response.json()

    def create_kiosk_sync(self, kiosk_data: dict) -> Any:
        """
        Создать новый киоск.
        """
        response = self._client.post("/api/kiosks", json=kiosk_data)
        response.raise_for_status()
        return response.json()

    async def create_kiosk_async(self, kiosk_data: dict) -> Any:
        """
        Создать новый киоск (async).
        """
        response = await self._client.post("/api/kiosks", json=kiosk_data)
        response.raise_for_status()
        return response.json()

    def update_kiosk_sync(self, kiosk_id: str, kiosk_data: dict) -> Any:
        """
        Изменить настройки киоска.
        """
        response = self._client.put(f"/api/kiosks/{kiosk_id}", json=kiosk_data)
        response.raise_for_status()
        return response.json()

    async def update_kiosk_async(self, kiosk_id: str, kiosk_data: dict) -> Any:
        """
        Изменить настройки киоска (async).
        """
        response = await self._client.put(f"/api/kiosks/{kiosk_id}", json=kiosk_data)
        response.raise_for_status()
        return response.json()

    def delete_kiosk_sync(self, kiosk_id: str) -> Any:
        """
        Удалить киоск.
        """
        response = self._client.delete(f"/api/kiosks/{kiosk_id}")
        response.raise_for_status()
        return response.json()

    async def delete_kiosk_async(self, kiosk_id: str) -> Any:
        """
        Удалить киоск (async).
        """
        response = await self._client.delete(f"/api/kiosks/{kiosk_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_kiosks(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_kiosks_async(*args, **kwargs)
        else:
            return self.get_kiosks_sync(*args, **kwargs)

    def get_kiosk_by_id(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_kiosk_by_id_async(*args, **kwargs)
        else:
            return self.get_kiosk_by_id_sync(*args, **kwargs)

    def create_kiosk(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_kiosk_async(*args, **kwargs)
        else:
            return self.create_kiosk_sync(*args, **kwargs)

    def update_kiosk(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_kiosk_async(*args, **kwargs)
        else:
            return self.update_kiosk_sync(*args, **kwargs)

    def delete_kiosk(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_kiosk_async(*args, **kwargs)
        else:
            return self.delete_kiosk_sync(*args, **kwargs)