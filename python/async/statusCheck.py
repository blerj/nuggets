import asyncio

import aiohttp

SITES = [
    "google.com",
    "cloudflare.com"
]

# Async function to get the status of the site using the given session
async def check_site(session, site):
    print(f"Requesting {site}")
    try:
        async with session.get(f"http://{site}") as resp:
            print(resp.status)
            return resp.status == 200
    except Exception as e:
        print(e)
        return False

# Check a list of sites asynchronously
async def health_check(sites):
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks, and run them together with gather
        tasks = [check_site(session, site) for site in sites]
        results = await asyncio.gather(*tasks)
        print(results)


async def main():
    await health_check(SITES)


asyncio.run(main())
