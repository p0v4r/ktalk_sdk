"""KTalk API Client Implementation."""

import httpx
from typing import Optional
from .api_keys import ApplicationsModule
from .recordings import RecordingsModule
from .meetings import MeetingsModule
from .kiosks import KiosksModule
from .rooms import RoomsModule
from .polls import PollsModule
from .reporting import ReportingModule
from .users import UsersModule
from .roles import RolesModule
from .statistics import StatisticsModule
from .calendar import CalendarModule


class BaseKTalkClient:
    """Base class for KTalk clients."""

    def __init__(self, base_url: str, token: str):
        """
        Initialize the client.

        Args:
            base_url: The base URL of the KTalk instance (e.g., https://your-space.ktalk.ru)
            token: The API token for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.token = token
        self._client: Optional[httpx.Client] = None
        self._async_client: Optional[httpx.AsyncClient] = None

    def _get_headers(self):
        """Get headers for API requests."""
        return {
            "X-Auth-Token": self.token,
            "Content-Type": "application/json",
        }


class KTalkClient(BaseKTalkClient):
    """Synchronous KTalk API Client."""

    def __init__(self, base_url: str, token: str):
        super().__init__(base_url, token)
        
        # Create synchronous client
        self._client = httpx.Client(
            base_url=self.base_url,
            headers=self._get_headers(),
        )
        
        # Initialize API modules
        self.applications = ApplicationsModule(self._client)
        self.recordings = RecordingsModule(self._client)
        self.meetings = MeetingsModule(self._client)
        self.kiosks = KiosksModule(self._client)
        self.rooms = RoomsModule(self._client)
        self.polls = PollsModule(self._client)
        self.reporting = ReportingModule(self._client)
        self.users = UsersModule(self._client)
        self.roles = RolesModule(self._client)
        self.statistics = StatisticsModule(self._client)
        self.calendar = CalendarModule(self._client)

    def close(self):
        """Close the client connection."""
        if self._client:
            self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class KTalkAsyncClient(BaseKTalkClient):
    """Asynchronous KTalk API Client."""

    def __init__(self, base_url: str, token: str):
        super().__init__(base_url, token)
        
        # Create asynchronous client
        self._async_client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self._get_headers(),
        )
        
        # Initialize API modules
        self.applications = ApplicationsModule(self._async_client)
        self.recordings = RecordingsModule(self._async_client)
        self.meetings = MeetingsModule(self._async_client)
        self.kiosks = KiosksModule(self._async_client)
        self.rooms = RoomsModule(self._async_client)
        self.polls = PollsModule(self._async_client)
        self.reporting = ReportingModule(self._async_client)
        self.users = UsersModule(self._async_client)
        self.roles = RolesModule(self._async_client)
        self.statistics = StatisticsModule(self._async_client)
        self.calendar = CalendarModule(self._async_client)

    async def aclose(self):
        """Close the async client connection."""
        if self._async_client:
            await self._async_client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()