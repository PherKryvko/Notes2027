import time
import asyncio


async def test():
    start = time.perf_counter()
    await asyncio.sleep(1)
    await asyncio.to_thread(time.sleep, 1)
    end = time.perf_counter() - start
    print(end)
    return "eewewew"


async def main():
    await test()
    await asyncio.gather(test(), test())
    print("DONE")

asyncio.run(main())