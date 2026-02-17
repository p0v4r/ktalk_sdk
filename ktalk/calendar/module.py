"""Calendar module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class CalendarModule:
    """Module for managing calendar in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_calendar_events_sync(self, from_date: str = None, to_date: str = None) -> Any:
        """
        Получить события календаря.
        """
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = self._client.get("/api/calendar/events", params=params)
        response.raise_for_status()
        return response.json()

    async def get_calendar_events_async(self, from_date: str = None, to_date: str = None) -> Any:
        """
        Получить события календаря (async).
        """
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = await self._client.get("/api/calendar/events", params=params)
        response.raise_for_status()
        return response.json()

    def get_calendar_event_by_id_sync(self, event_id: str) -> Any:
        """
        Получить событие календаря по ID.
        """
        response = self._client.get(f"/api/calendar/events/{event_id}")
        response.raise_for_status()
        return response.json()

    async def get_calendar_event_by_id_async(self, event_id: str) -> Any:
        """
        Получить событие календаря по ID (async).
        """
        response = await self._client.get(f"/api/calendar/events/{event_id}")
        response.raise_for_status()
        return response.json()

    def create_calendar_event_sync(self, event_data: dict) -> Any:
        """
        Создать новое событие календаря.
        """
        response = self._client.post("/api/calendar/events", json=event_data)
        response.raise_for_status()
        return response.json()

    async def create_calendar_event_async(self, event_data: dict) -> Any:
        """
        Создать новое событие календаря (async).
        """
        response = await self._client.post("/api/calendar/events", json=event_data)
        response.raise_for_status()
        return response.json()

    def update_calendar_event_sync(self, event_id: str, event_data: dict) -> Any:
        """
        Изменить настройки события календаря.
        """
        response = self._client.put(f"/api/calendar/events/{event_id}", json=event_data)
        response.raise_for_status()
        return response.json()

    async def update_calendar_event_async(self, event_id: str, event_data: dict) -> Any:
        """
        Изменить настройки события календаря (async).
        """
        response = await self._client.put(f"/api/calendar/events/{event_id}", json=event_data)
        response.raise_for_status()
        return response.json()

    def delete_calendar_event_sync(self, event_id: str) -> Any:
        """
        Удалить событие календаря.
        """
        response = self._client.delete(f"/api/calendar/events/{event_id}")
        response.raise_for_status()
        return response.json()

    async def delete_calendar_event_async(self, event_id: str) -> Any:
        """
        Удалить событие календаря (async).
        """
        response = await self._client.delete(f"/api/calendar/events/{event_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_calendar_events(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_calendar_events_async(*args, **kwargs)
        else:
            return self.get_calendar_events_sync(*args, **kwargs)

    def get_calendar_event_by_id(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_calendar_event_by_id_async(*args, **kwargs)
        else:
            return self.get_calendar_event_by_id_sync(*args, **kwargs)

    def create_calendar_event(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.create_calendar_event_async(*args, **kwargs)
        else:
            return self.create_calendar_event_sync(*args, **kwargs)

    def update_calendar_event(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.update_calendar_event_async(*args, **kwargs)
        else:
            return self.update_calendar_event_sync(*args, **kwargs)

    def delete_calendar_event(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.delete_calendar_event_async(*args, **kwargs)
        else:
            return self.delete_calendar_event_sync(*args, **kwargs)