import requests, httpx, asyncio, time
import json
# import requests_ntlm
from urllib.parse import urlsplit, quote, urlparse
import dateparser


if __name__=="__main__":
    all_data = []
    async def fetch():
        res_obj = []
        async with httpx.AsyncClient() as client:    
            res = [client.get(f"https://ghoapi.azureedge.net/api/Rev_curr?$select=Id&$top={i}",timeout=20) for i in range(1,101)]
            data = await asyncio.gather(*res)
            for d in data:
                all_data.extend(d.json()['value'])
        print(data)
        with open('test.json', 'w',encoding='utf8') as f:
            f.write(json.dumps(all_data, indent=4, ensure_ascii=False))

start = time.perf_counter()
asyncio.run(fetch())
end = time.perf_counter()

print(end - start)