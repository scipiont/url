import aiohttp
import asyncio

async def download_url(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
            filename = url.replace("http://", "").replace("https://", "").replace("/", "_") + ".html"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"{url} downloaded as {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    with open('urls.txt', 'r') as file:
        urls = [line.strip() for line in file]
    asyncio.run(main(urls))
