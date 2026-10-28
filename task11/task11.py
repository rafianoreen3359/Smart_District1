""" Task: 
● Async Data Sync Dashboard: A data team needs a tool that simultaneously pulls data 
from three mock sources, merges the results, and displays a combined summary. It must 
run inside a virtual environment with all credentials stored in a `.env` file outside the 
codebase."""
import asyncio
import os

async def source_one():
    await asyncio.sleep(2)
    return {"sales": 100, "users": 20}

async def source_two():
    await asyncio.sleep(1)
    return {"sales": 200, "orders": 15}

async def source_three():
    await asyncio.sleep(3)
    return {"users": 30, "orders": 25}

async def main():
    print("Syncing data from 3 sources...")

    results = await asyncio.gather(
        source_one(),
        source_two(),
        source_three()
    )

    combined = {}

    for result in results:
        for key, value in result.items():
            combined[key] = combined.get(key, 0) + value

    print("\n===== DATA SYNC DASHBOARD =====")

    for key, value in combined.items():
        print(f"{key.title()}: {value}")


asyncio.run(main())
