# KTalk SDK

Python SDK for KTalk API integration.

## Installation

```bash
pip install ktalk-sdk
```

## Usage

```python
from ktalk import KTalkClient

# Initialize the client
client = KTalkClient(base_url="https://your-space.ktalk.ru", token="your-api-token")

# Use the API
users = client.users.get_users()
```

For asynchronous operations:

```python
import asyncio
from ktalk import KTalkAsyncClient

async def main():
    async with KTalkAsyncClient(base_url="https://your-space.ktalk.ru", token="your-api-token") as client:
        users = await client.users.get_users()

asyncio.run(main())
```

## Features

- Full coverage of KTalk API endpoints
- Synchronous and asynchronous client implementations
- Type-safe models generated from API specification
- Organized into logical modules based on API tags

## API Modules

The SDK is organized into the following modules based on the KTalk API:

- API Keys (`client.applications`)
- Recordings (`client.recordings`)
- Meetings (`client.meetings`)
- Kiosks (`client.kiosks`)
- Rooms (`client.rooms`)
- Polls (`client.polls`)
- Reporting (`client.reporting`)
- Users (`client.users`)
- Roles (`client.roles`)
- Statistics (`client.statistics`)
- Calendar Management (`client.calendar`)

## License

MIT