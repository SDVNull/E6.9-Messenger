import asyncio


# async def count_to(n):
#     for i in range(1, n + 1):
#         print(i)
#         await asyncio.sleep(1)


# async def main():
#     await asyncio.gather(
#         count_to(3),
#         count_to(5),
#         count_to(10),
#     )
#     print("All done!")


# asyncio.run(main())


async def download(url):
    print(f"Start {url}")
    await asyncio.sleep(2)
    print(f"Finish {url}")


# async def monitor(interval):
#     if type(interval) is not int:
#         raise TypeError("Interval must be an integer")
#     else:
#         while True:
#             print("System OK")
#             await asyncio.sleep(interval)


# async def main() -> None:
#     """Run monitoring and download tasks concurrently."""
#     tasks = [
#         asyncio.create_task(monitor(2)),
#         asyncio.create_task(download("https://google.com")),
#         asyncio.create_task(download("https://yandex.ru")),
#         asyncio.create_task(download("https://vk.com"))
#     ]

#     await asyncio.gather(tasks[1], tasks[2], tasks[3])
#     await asyncio.wait({tasks[0]}, timeout=1)
#     print("All done!")
#     tasks[0].cancel()


# asyncio.run(main())
async def download(url):
    print(f"Start {url}")
    await asyncio.sleep(2)
    print(f"Finish {url}")


async def monitor(interval):
    try:
        while True:
            print("System OK")
            await asyncio.sleep(interval)
    except asyncio.CancelledError:
        print("Monitor stopped")


async def main():
    monitor_task = asyncio.create_task(monitor(2))

    download_tasks = [
        asyncio.create_task(download(url))
        for url in ["https://google.com", "https://yandex.ru", "https://vk.com"]
    ]

    for task in download_tasks:
        await task
    print(monitor_task.cancelled())
    monitor_task.cancel()
    print(monitor_task.cancelled())
    print("All done!")


asyncio.run(main())
