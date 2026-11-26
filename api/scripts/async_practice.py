import time
import asyncio #lib

async def Prac(seconds: float) -> str: #async method to allow awaits
    start = time.perf_counter()
    await asyncio.sleep(seconds) #await asyncio.sleep(time) to pause xyz time 
    print(f"{time.perf_counter() - start:.1f}")
    
    await asyncio.to_thread(time.sleep, 1) #send await to another helper thread 
    
    return "Done"

async def main() -> None:
    print(await(Prac(1))) #await then method to call methods 
    
    start = time.perf_counter()
    return_two = await asyncio.gather(Prac(1), Prac(3))
    print(f"DUAL: {time.perf_counter() - start:.1f}")
    
asyncio.run(main()) #Start async up, only 1 per thread
