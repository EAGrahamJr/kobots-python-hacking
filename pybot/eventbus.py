import asyncio
from collections.abc import Callable, Awaitable
from typing import Any, Dict, List


class EventBus:
    """
    An asyncio event bus -- mostly "written" by Copilot with appropriate prompting.

    Handlers must be asyncio functions and can take named arguments.
    """

    def __init__(self) -> None:
        self._listeners: Dict[str, List[Callable[..., Awaitable[None]]]] = {}

    def on(self, event: str, handler: Callable[..., Awaitable[None]]) -> None:
        """Register an async handler for a given event."""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(handler)

    async def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Emit an event and schedule all handlers without waiting for them."""
        if event not in self._listeners:
            return
        for handler in self._listeners[event]:
            # Schedule each handler as a background task
            asyncio.create_task(handler(*args, **kwargs))  # type: ignore
