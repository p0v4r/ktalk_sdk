"""Recordings module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class RecordingsModule:
    """Module for managing recordings in KTalk."""
    
    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_recordings_list_sync(self, top: int = 50, start: str = None) -> Any:
        """Получить список записей."""
        params = {"top": top}
        if start:
            params["start"] = start
            
        response = self._client.get("/api/recordings", params=params)
        response.raise_for_status()
        return response.json()

    async def get_recordings_list_async(self, top: int = 50, start: str = None) -> Any:
        """Получить список записей (async)."""
        params = {"top": top}
        if start:
            params["start"] = start
            
        response = await self._client.get("/api/recordings", params=params)
        response.raise_for_status()
        return response.json()

    def get_recording_by_key_sync(self, recording_key: str) -> Any:
        """Получить информацию о записи по ключу."""
        response = self._client.get(f"/api/recordings/{recording_key}")
        response.raise_for_status()
        return response.json()

    async def get_recording_by_key_async(self, recording_key: str) -> Any:
        """Получить информацию о записи по ключу (async)."""
        response = await self._client.get(f"/api/recordings/{recording_key}")
        response.raise_for_status()
        return response.json()

    def get_recording_summary_sync(self, recording_key: str) -> Any:
        """Получить краткое описание записи."""
        response = self._client.get(f"/api/recordings/{recording_key}/summary")
        response.raise_for_status()
        return response.json()

    async def get_recording_summary_async(self, recording_key: str) -> Any:
        """Получить краткое описание записи (async)."""
        response = await self._client.get(f"/api/recordings/{recording_key}/summary")
        response.raise_for_status()
        return response.json()

    def get_recording_download_link_sync(self, recording_key: str) -> Any:
        """Получить ссылку для скачивания записи."""
        response = self._client.get(f"/api/recordings/{recording_key}/download-link")
        response.raise_for_status()
        return response.json()

    async def get_recording_download_link_async(self, recording_key: str) -> Any:
        """Получить ссылку для скачивания записи (async)."""
        response = await self._client.get(f"/api/recordings/{recording_key}/download-link")
        response.raise_for_status()
        return response.json()

    def update_recording_sync(self, recording_key: str, recording_data: dict) -> Any:
        """Изменить информацию о записи."""
        response = self._client.put(f"/api/recordings/{recording_key}", json=recording_data)
        response.raise_for_status()
        return response.json()

    async def update_recording_async(self, recording_key: str, recording_data: dict) -> Any:
        """Изменить информацию о записи (async)."""
        response = await self._client.put(f"/api/recordings/{recording_key}", json=recording_data)
        response.raise_for_status()
        return response.json()

    def delete_recording_sync(self, recording_key: str) -> Any:
        """Удалить запись."""
        response = self._client.delete(f"/api/recordings/{recording_key}")
        response.raise_for_status()
        return response.json()

    async def delete_recording_async(self, recording_key: str) -> Any:
        """Удалить запись (async)."""
        response = await self._client.delete(f"/api/recordings/{recording_key}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_recordings_list(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_recordings_list_async(*args, **kwargs)
        else:
            return self.get_recordings_list_sync(*args, **kwargs)

    def get_recording_by_key(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_recording_by_key_async(*args, **kwargs)
        else:
            return self.get_recording_by_key_sync(*args, **kwargs)

    def get_recording_summary(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_recording_summary_async(*args, **kwargs)
        else:
            return self.get_recording_summary_sync(*args, **kwargs)

    def get_recording_download_link(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_recording_download_link_async(*args, **kwargs)
        else:
            return self.get_recording_download_link_sync(*args, **kwargs)

    def update_recording(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_recording_async(*args, **kwargs)
        else:
            return self.update_recording_sync(*args, **kwargs)

    def delete_recording(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_recording_async(*args, **kwargs)
        else:
            return self.delete_recording_sync(*args, **kwargs)