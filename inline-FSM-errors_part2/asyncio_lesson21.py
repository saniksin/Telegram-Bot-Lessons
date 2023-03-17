import asyncio 

async def send_time(sec: int) -> None:
    while True:
        await asyncio.sleep(sec)
        print(f'Прошло {sec} секунд')

# 2 РАЗНЫХ ОБЪЕКТА КОРУТИНЫ
#print(send_time(2), send_time(5), sep='\n')
#<coroutine object send_time at 0x7fa8b30c3680>
#<coroutine object send_time at 0x7fa8b30c3d10>

async def main() -> None:
    task_1 = asyncio.create_task(send_time(2))
    task_2 = asyncio.create_task(send_time(5))

    await task_1
    await task_2


if __name__ == "__main__":
    asyncio.run(main())