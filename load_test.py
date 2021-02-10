import asyncio
import aiohttp
import time

web='http://my-nginx:8080'
urls=[]

for _ in range(1,11):
    urls.append(web)

async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                print("Status:", response.status,end=" ")
                html = await response.text()
                print(html[11:20])
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))

async def main(urls, amount):
    ret = await asyncio.gather(*[get(url) for url in urls])

amount = len(urls)

start = time.time()
asyncio.run(main(urls, amount))
end = time.time()

#print("Took {} seconds to pull {} websites.".format(end - start, amount))
