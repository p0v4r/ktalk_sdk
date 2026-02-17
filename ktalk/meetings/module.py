"""Meetings module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class MeetingsModule:
    """Module for managing meetings in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_meetings_sync(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список встреч.
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = self._client.get("/api/meetings", params=params)
        response.raise_for_status()
        return response.json()

    async def get_meetings_async(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список встреч (async).
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = await self._client.get("/api/meetings", params=params)
        response.raise_for_status()
        return response.json()

    def get_meeting_by_id_sync(self, meeting_id: str) -> Any:
        """
        Получить информацию о встрече по ID.
        """
        response = self._client.get(f"/api/meetings/{meeting_id}")
        response.raise_for_status()
        return response.json()

    async def get_meeting_by_id_async(self, meeting_id: str) -> Any:
        """
        Получить информацию о встрече по ID (async).
        """
        response = await self._client.get(f"/api/meetings/{meeting_id}")
        response.raise_for_status()
        return response.json()

    def create_meeting_sync(self, meeting_data: dict) -> Any:
        """
        Создать новую встречу.
        """
        response = self._client.post("/api/meetings", json=meeting_data)
        response.raise_for_status()
        return response.json()

    async def create_meeting_async(self, meeting_data: dict) -> Any:
        """
        Создать новую встречу (async).
        """
        response = await self._client.post("/api/meetings", json=meeting_data)
        response.raise_for_status()
        return response.json()

    def update_meeting_sync(self, meeting_id: str, meeting_data: dict) -> Any:
        """
        Изменить настройки встречи.
        """
        response = self._client.put(f"/api/meetings/{meeting_id}", json=meeting_data)
        response.raise_for_status()
        return response.json()

    async def update_meeting_async(self, meeting_id: str, meeting_data: dict) -> Any:
        """
        Изменить настройки встречи (async).
        """
        response = await self._client.put(f"/api/meetings/{meeting_id}", json=meeting_data)
        response.raise_for_status()
        return response.json()

    def delete_meeting_sync(self, meeting_id: str) -> Any:
        """
        Удалить встречу.
        """
        response = self._client.delete(f"/api/meetings/{meeting_id}")
        response.raise_for_status()
        return response.json()

    async def delete_meeting_async(self, meeting_id: str) -> Any:
        """
        Удалить встречу (async).
        """
        response = await self._client.delete(f"/api/meetings/{meeting_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_meetings(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_meetings_async(*args, **kwargs)
        else:
            return self.get_meetings_sync(*args, **kwargs)

    def get_meeting_by_id(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_meeting_by_id_async(*args, **kwargs)
        else:
            return self.get_meeting_by_id_sync(*args, **kwargs)

    def create_meeting(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_meeting_async(*args, **kwargs)
        else:
            return self.create_meeting_sync(*args, **kwargs)

    def update_meeting(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_meeting_async(*args, **kwargs)
        else:
            return self.update_meeting_sync(*args, **kwargs)

    def delete_meeting(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_meeting_async(*args, **kwargs)
        else:
            return self.delete_meeting_sync(*args, **kwargs)