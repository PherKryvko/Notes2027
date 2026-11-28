"""Reference solutions. Open only after you have tried each drill."""
import asyncio
import time


async def fake_call(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)
    return f"{name} done"


async def run_together(a_seconds: float, b_seconds: float) -> list[str]:
    # gather starts both, lets the waits overlap, returns results in the order listed
    return await asyncio.gather(fake_call("a", a_seconds), fake_call("b", b_seconds))


async def get_label(name: str) -> str:
    result = await fake_call(name, 0.05)  # the fix: without await you only get a coroutine
    return result


async def blocky(name: str, seconds: float) -> str:
    await asyncio.to_thread(time.sleep, seconds)  # blocking call moved to a helper thread
    return f"{name} done"


async def run_limited(seconds_list: list[float], limit: int) -> list[str]:
    gate = asyncio.Semaphore(limit)

    async def one(i: int, seconds: float) -> str:
        async with gate:
            return await fake_call(str(i), seconds)

    return await asyncio.gather(*(one(i, s) for i, s in enumerate(seconds_list)))


async def with_fallback(seconds: float, limit: float) -> str:
    try:
        async with asyncio.timeout(limit):
            return await fake_call("tts", seconds)
    except TimeoutError:
        return "fallback"


async def tokens(text: str):
    for word in text.split():
        await asyncio.sleep(0.01)
        yield word


async def safe_bump(counter: dict[str, int], lock: asyncio.Lock) -> None:
    async with lock:  # the whole read-await-write is one step for the other calls
        value = counter["n"]
        await asyncio.sleep(0)
        counter["n"] = value + 1


async def run_with_signal(delay: float) -> str:
    event = asyncio.Event()

    async def waiter() -> str:
        await event.wait()
        return "go"

    async def setter() -> None:
        await asyncio.sleep(delay)
        event.set()

    results = await asyncio.gather(waiter(), setter())
    return results[0]


async def pipe(items: list[int]) -> list[int]:
    queue: asyncio.Queue = asyncio.Queue(maxsize=1)
    out: list[int] = []

    async def producer() -> None:
        for item in items:
            await queue.put(item)
        await queue.put(None)  # sentinel: no more items

    async def consumer() -> None:
        while (item := await queue.get()) is not None:
            out.append(item)

    await asyncio.gather(producer(), consumer())
    return out
