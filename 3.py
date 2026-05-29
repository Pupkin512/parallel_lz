import asyncio
async def sol():
    coun = 0
    lock = asyncio.Lock()
    async def proc():
        nonlocal coun
        async with lock:
            await asyncio.sleep(0.01)
            coun = coun + 1
    tasks = [proc(i) for i in range(100)]
    await asyncio.gather(*tasks)
    print(f"Итоговое значение счетчика: {coun}")
