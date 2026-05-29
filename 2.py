import asyncio, random, time
async def processеtxt():
    sem = asyncio.Semaphore(10)
    async def task(task_id):
        async with sem:
            await asyncio.sleep(random.randint(5, 10))
            print(f"файл {task_id:1} обработан")
    nachalo = time.perf_counter()
    tasks = [task(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)
    print(f"\nОбщее время выполнения парралельно: {time.perf_counter() - nachalo:.2f} сек.")
    sem = asyncio.Semaphore(1)   
    async def task(task_id):
        async with sem:
            await asyncio.sleep(random.randint(5, 10))
            print(f"Файл {task_id:1} обработан")
    nachalo = time.perf_counter()
    tasks = [task(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)
    print(f"\nОбщее время выполнения последовательно: {time.perf_counter() - nachalo:.2f} сек.")