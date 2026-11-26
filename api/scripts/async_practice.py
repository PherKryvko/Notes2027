import time
import asyncio #lib

async def Prac(seconds: float) -> str: #async method to allow awaits
    await asyncio.sleep(seconds) #await asyncio.sleep(time) to pause xyz time 
    
    return "Done"

async def main() -> None:
    print(await(Prac(1))) #await then method to call methods 
    
asyncio.run(main()) #Start async up, only 1 per thread