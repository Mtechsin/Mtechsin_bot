import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    while True:
        print(datetime.datetime.now())
        await asyncio.sleep(1)

asyncio.run(display_date())