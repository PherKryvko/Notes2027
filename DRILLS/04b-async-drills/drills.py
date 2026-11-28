"""Async drills. Edit this file, then run the tests (see the 04b note).

Work top to bottom. Do not open solutions.py until you have tried.
Timings use small waits (0.2 s) so the tests run quickly.
"""
import asyncio
import time


async def fake_call(name: str, seconds: float) -> str:
    """Pretend to wait for a network reply. Already correct: do not change."""
    await asyncio.sleep(seconds)
    return f"{name} done"


# ---------------------------------------------------------------------------
# Drill 1: run two calls at the same time
# Return the two results as a list, in the order a then b. It must take about
# as long as the SLOWER call, not the sum of both.
# ---------------------------------------------------------------------------
async def run_together(a_seconds: float, b_seconds: float) -> list[str]:
   values = await asyncio.gather(fake_call("a", a_seconds), fake_call("b", b_seconds))
   return values 
    


# ---------------------------------------------------------------------------
# Drill 2: fix the bug
# get_label should return "x done", but it returns something else. Fix it.
# ---------------------------------------------------------------------------
async def get_label(name: str) -> str:
    result = await fake_call(name, 0.05)
    return result


# ---------------------------------------------------------------------------
# Drill 3: fix the bug
# Two blocky() calls run with gather should overlap (about 0.2 s in total),
# but right now they take twice as long. Fix it WITHOUT changing the wait
# itself: keep calling time.sleep, but stop it freezing the event loop.
# ---------------------------------------------------------------------------
async def blocky(name: str, seconds: float) -> str:
    await asyncio.to_thread(time.sleep, seconds)
    return f"{name} done"


# ---------------------------------------------------------------------------
# Drill 4: limit how many run at once
# Run one fake_call per entry in `seconds_list`, but never more than `limit`
# at the same time. Return the results in the same order as seconds_list.
# ---------------------------------------------------------------------------
async def run_limited(seconds_list: list[float], limit: int) -> list[str]:
    gate = asyncio.Semaphore(limit)

    async def one(i: int, seconds: float) -> str:
        async with gate:
            return await fake_call(str(i), seconds)

    tasks = []
    for i, seconds in enumerate(seconds_list):
        tasks.append(one(i, seconds))

    return await asyncio.gather(*tasks)

async def simplified():
    gate = asyncio.Semaphore(2)
    
    async def method_to_list():
        async with gate:
            return await fake_call("a", 1)

    tasks = []
    
    fake_amount = [1,2,3]
    for i, vars in enumerate(fake_amount):
        tasks.append(method_to_list())
        
    return await asyncio.gather(*tasks)
        
# ---------------------------------------------------------------------------
# Drill 5: time limit with a fallback
# Wait for fake_call("tts", seconds). If it takes longer than `limit` seconds,
# give up and return "fallback". Otherwise return its result.
# ---------------------------------------------------------------------------
async def with_fallback(seconds: float, limit: float) -> str:
    
    try:
        async with asyncio.timeout(limit):
            return await fake_call("tts", seconds)
    except TimeoutError:
        return "fallback"

# ---------------------------------------------------------------------------
# Drill 6: a stream of results
# Make tokens() an async generator that yields each word of `text` one at a
# time, pausing 0.01 s (await asyncio.sleep) before each.
# ---------------------------------------------------------------------------
def tokens(text: str):
    raise NotImplementedError  # TODO: this needs to become an async generator


# ---------------------------------------------------------------------------
# Drill 7: a lock
# counter["n"] must go up by exactly 1 per call, even when 10 calls run at the
# same time. Read the value, await asyncio.sleep(0), then write value + 1.
# Put ALL of that inside `async with lock:` so no other call can interleave.
# ---------------------------------------------------------------------------
async def safe_bump(counter: dict[str, int], lock: asyncio.Lock) -> None:
    raise NotImplementedError  # TODO


# ---------------------------------------------------------------------------
# Drill 8: an event
# Start a waiter that waits for an asyncio.Event, and a setter that calls
# event.set() after `delay` seconds. Return what the waiter returns: "go".
# Both must run at the same time, so it takes about `delay` seconds.
# ---------------------------------------------------------------------------
async def run_with_signal(delay: float) -> str:
    raise NotImplementedError  # TODO


# ---------------------------------------------------------------------------
# Drill 9: a queue
# A producer puts each item into an asyncio.Queue(maxsize=1), then puts None
# as "no more". A consumer gets items until it sees None and collects them.
# Both run at the same time (the queue holds only one item, so they must
# overlap). Return the collected items.
# ---------------------------------------------------------------------------
async def pipe(items: list[int]) -> list[int]:
    raise NotImplementedError  # TODO
