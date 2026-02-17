"""Rooms module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class RoomsModule:
    """Module for managing rooms in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_rooms_sync(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список комнат.
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = self._client.get("/api/rooms", params=params)
        response.raise_for_status()
        return response.json()

    async def get_rooms_async(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список комнат (async).
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = await self._client.get("/api/rooms", params=params)
        response.raise_for_status()
        return response.json()

    def get_room_by_name_sync(self, room_name: str) -> Any:
        """
        Получить информацию о комнате по имени.
        """
        response = self._client.get(f"/api/rooms/{room_name}")
        response.raise_for_status()
        return response.json()

    async def get_room_by_name_async(self, room_name: str) -> Any:
        """
        Получить информацию о комнате по имени (async).
        """
        response = await self._client.get(f"/api/rooms/{room_name}")
        response.raise_for_status()
        return response.json()

    def create_room_sync(self, room_data: dict) -> Any:
        """
        Создать новую комнату.
        """
        response = self._client.post("/api/rooms", json=room_data)
        response.raise_for_status()
        return response.json()

    async def create_room_async(self, room_data: dict) -> Any:
        """
        Создать новую комнату (async).
        """
        response = await self._client.post("/api/rooms", json=room_data)
        response.raise_for_status()
        return response.json()

    def update_room_sync(self, room_name: str, room_data: dict) -> Any:
        """
        Изменить настройки комнаты.
        """
        response = self._client.put(f"/api/rooms/{room_name}", json=room_data)
        response.raise_for_status()
        return response.json()

    async def update_room_async(self, room_name: str, room_data: dict) -> Any:
        """
        Изменить настройки комнаты (async).
        """
        response = await self._client.put(f"/api/rooms/{room_name}", json=room_data)
        response.raise_for_status()
        return response.json()

    def delete_room_sync(self, room_name: str) -> Any:
        """
        Удалить комнату.
        """
        response = self._client.delete(f"/api/rooms/{room_name}")
        response.raise_for_status()
        return response.json()

    async def delete_room_async(self, room_name: str) -> Any:
        """
        Удалить комнату (async).
        """
        response = await self._client.delete(f"/api/rooms/{room_name}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_rooms(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_rooms_async(*args, **kwargs)
        else:
            return self.get_rooms_sync(*args, **kwargs)

    def get_room_by_name(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_room_by_name_async(*args, **kwargs)
        else:
            return self.get_room_by_name_sync(*args, **kwargs)

    def create_room(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_room_async(*args, **kwargs)
        else:
            return self.create_room_sync(*args, **kwargs)

    def update_room(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_room_async(*args, **kwargs)
        else:
            return self.update_room_sync(*args, **kwargs)

    def delete_room(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_room_async(*args, **kwargs)
        else:
            return self.delete_room_sync(*args, **kwargs)