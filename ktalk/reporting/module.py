"""Reporting module for KTalk API."""

from typing import TYPE_CHECKING, Union, List, Any
import httpx

if TYPE_CHECKING:
    from httpx._types import AnyIO


class ReportingModule:
    """Module for managing reporting in KTalk."""

    def __init__(self, client: Union[httpx.Client, httpx.AsyncClient]):
        self._client = client

    def get_reports_sync(self, report_type: str = None, from_date: str = None, to_date: str = None) -> Any:
        """
        Получить отчеты.
        """
        params = {}
        if report_type:
            params["type"] = report_type
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = self._client.get("/api/reports", params=params)
        response.raise_for_status()
        return response.json()

    async def get_reports_async(self, report_type: str = None, from_date: str = None, to_date: str = None) -> Any:
        """
        Получить отчеты (async).
        """
        params = {}
        if report_type:
            params["type"] = report_type
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = await self._client.get("/api/reports", params=params)
        response.raise_for_status()
        return response.json()

    def get_report_by_id_sync(self, report_id: str) -> Any:
        """
        Получить отчет по ID.
        """
        response = self._client.get(f"/api/reports/{report_id}")
        response.raise_for_status()
        return response.json()

    async def get_report_by_id_async(self, report_id: str) -> Any:
        """
        Получить отчет по ID (async).
        """
        response = await self._client.get(f"/api/reports/{report_id}")
        response.raise_for_status()
        return response.json()

    # Select implementation based on client type
    def get_reports(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_reports_async(*args, **kwargs)
        else:
            return self.get_reports_sync(*args, **kwargs)

    def get_report_by_id(self, *args, **kwargs):
        if isinstance(self._client, httpx.AsyncClient):
            return self.get_report_by_id_async(*args, **kwargs)
        else:
            return self.get_report_by_id_sync(*args, **kwargs)