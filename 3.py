import asyncio
async def sol():
    counter = 0
    lock = asyncio.Lock()
    async def proc():
        nonlocal counter
        async with lock:
            await asyncio.sleep(0.01)
            counter = counter + 1
    tasks = [proc(i) for i in range(100)]
    await asyncio.gather(*tasks)
    print(f"Итоговое значение счетчика: {counter}")