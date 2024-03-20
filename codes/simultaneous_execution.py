import time
import asyncio

async def func1():
    await asyncio.sleep(1)
    print("func1")
    
async def func2():
    await asyncio.sleep(1)
    print("func2")
    
async def func3():
    await asyncio.sleep(1)
    print("func3")
    
async def main():
    L=await asyncio.gather(func1(),func2(),func3())
    print(L)
    
asyncio.run(main())