"""Statistics module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class StatisticsModule:
    """Module for managing statistics in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_statistics_sync(self, stat_type: str = None, from_date: str = None, to_date: str = None) -> Any:
        """
        Получить статистику.
        """
        params = {}
        if stat_type:
            params["type"] = stat_type
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = self._client.get("/api/statistics", params=params)
        response.raise_for_status()
        return response.json()

    async def get_statistics_async(self, stat_type: str = None, from_date: str = None, to_date: str = None) -> Any:
        """
        Получить статистику (async).
        """
        params = {}
        if stat_type:
            params["type"] = stat_type
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = await self._client.get("/api/statistics", params=params)
        response.raise_for_status()
        return response.json()

    def get_conference_statistics_sync(self, conference_id: str) -> Any:
        """
        Получить статистику конференции.
        """
        response = self._client.get(f"/api/statistics/conferences/{conference_id}")
        response.raise_for_status()
        return response.json()

    async def get_conference_statistics_async(self, conference_id: str) -> Any:
        """
        Получить статистику конференции (async).
        """
        response = await self._client.get(f"/api/statistics/conferences/{conference_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_statistics(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_statistics_async(*args, **kwargs)
        else:
            return self.get_statistics_sync(*args, **kwargs)

    def get_conference_statistics(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_conference_statistics_async(*args, **kwargs)
        else:
            return self.get_conference_statistics_sync(*args, **kwargs)