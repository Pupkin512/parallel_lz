import asyncio, random, time
async def sema():
    sem = asyncio.Semaphore(5)
    async def task(task_id):
        async with sem:
            await asyncio.sleep(random.randint(1, 2))
            print(f"Задача {task_id:1} завершена")
    nachalo.perf_counter()
    tasks = [task(i) for i in range(1, 101)]
    await asyncio.gather(*tasks)
    print(f"\nОбщее время : {time.perf_counter() - nachalo:.2f} сек.")
