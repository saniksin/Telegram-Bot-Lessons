import asyncio

async def one_second() -> None:
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        print(f'Прошло {n} секунд!' if n%3!=0 else '')

async def three_second() -> None:
    while True:
        await asyncio.sleep(3)
        print('Прошло три секунды')


async def main():
    task_1 = asyncio.create_task(one_second())
    task_2 = asyncio.create_task(three_second())

    await task_1
    await task_2


asyncio.run(main())