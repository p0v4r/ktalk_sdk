"""Polls module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class PollsModule:
    """Module for managing polls in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_polls_sync(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список опросов.
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = self._client.get("/api/polls", params=params)
        response.raise_for_status()
        return response.json()

    async def get_polls_async(self, top: int = 50, start: str = None) -> Any:
        """
        Получить список опросов (async).
        """
        params = {"top": top}
        if start:
            params["start"] = start

        response = await self._client.get("/api/polls", params=params)
        response.raise_for_status()
        return response.json()

    def get_poll_by_id_sync(self, poll_id: str) -> Any:
        """
        Получить информацию об опросе по ID.
        """
        response = self._client.get(f"/api/polls/{poll_id}")
        response.raise_for_status()
        return response.json()

    async def get_poll_by_id_async(self, poll_id: str) -> Any:
        """
        Получить информацию об опросе по ID (async).
        """
        response = await self._client.get(f"/api/polls/{poll_id}")
        response.raise_for_status()
        return response.json()

    def create_poll_sync(self, poll_data: dict) -> Any:
        """
        Создать новый опрос.
        """
        response = self._client.post("/api/polls", json=poll_data)
        response.raise_for_status()
        return response.json()

    async def create_poll_async(self, poll_data: dict) -> Any:
        """
        Создать новый опрос (async).
        """
        response = await self._client.post("/api/polls", json=poll_data)
        response.raise_for_status()
        return response.json()

    def update_poll_sync(self, poll_id: str, poll_data: dict) -> Any:
        """
        Изменить настройки опроса.
        """
        response = self._client.put(f"/api/polls/{poll_id}", json=poll_data)
        response.raise_for_status()
        return response.json()

    async def update_poll_async(self, poll_id: str, poll_data: dict) -> Any:
        """
        Изменить настройки опроса (async).
        """
        response = await self._client.put(f"/api/polls/{poll_id}", json=poll_data)
        response.raise_for_status()
        return response.json()

    def delete_poll_sync(self, poll_id: str) -> Any:
        """
        Удалить опрос.
        """
        response = self._client.delete(f"/api/polls/{poll_id}")
        response.raise_for_status()
        return response.json()

    async def delete_poll_async(self, poll_id: str) -> Any:
        """
        Удалить опрос (async).
        """
        response = await self._client.delete(f"/api/polls/{poll_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_polls(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_polls_async(*args, **kwargs)
        else:
            return self.get_polls_sync(*args, **kwargs)

    def get_poll_by_id(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_poll_by_id_async(*args, **kwargs)
        else:
            return self.get_poll_by_id_sync(*args, **kwargs)

    def create_poll(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_poll_async(*args, **kwargs)
        else:
            return self.create_poll_sync(*args, **kwargs)

    def update_poll(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_poll_async(*args, **kwargs)
        else:
            return self.update_poll_sync(*args, **kwargs)

    def delete_poll(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_poll_async(*args, **kwargs)
        else:
            return self.delete_poll_sync(*args, **kwargs)