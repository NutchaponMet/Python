import requests
from urllib.parse import quote
import json
import httpx
import asyncio
import time

# URL = f"https://ghoapi.azureedge.net/api/RSUD_490?$top={page_size}"page_size
URL1 = f"https://ghoapi.azureedge.net/api/RSUD_490"
# query_property = f"Id,IndicatorCode,SpatialDim,TimeDim,Dim1Type&$top={page_size}&$skip={skip}"
query_row = quote(f'Id ge {15984810} and Id le {15984840}')
# query = f"?$select={query_property}"

def getodata():
    st = time.time()
    odata_url = f"https://ghoapi.azureedge.net/api/RSUD_490"
    # จำนวนแถวที่ต้องการดึงในแต่ละรอบ
    page_size = 1000
    # ตัวแปรเพื่อเก็บข้อมูลทั้งหมด
    all_data = []
    # ตัวแปรเพื่อติดตามตำแหน่งเริ่มต้นของการดึงข้อมูล
    skip = 0
    while True:
        # สร้างคำสั่ง query OData ที่ระบุจำนวนแถวและตำแหน่งเริ่มต้นในการดึงข้อมูล
        query = f"?$top={page_size}&$skip={skip}"

        # ส่งคำขอ HTTP GET ไปยังแหล่งข้อมูล OData
        response = requests.get(odata_url + query)

        if response.status_code == 200:
            # รับข้อมูล JSON จากคำตอบ
            data = response.json()

            # เพิ่มข้อมูลที่ได้ลงในรายการ all_data
            all_data.extend(data['value'])

            # ตรวจสอบว่ายังมีข้อมูลอีกหรือไม่
            if len(data['value']) < page_size:
                break  # ไม่มีข้อมูลอีก หยุดการดึงข้อมูล
            else:
                skip += page_size  # เพิ่มตำแหน่งเริ่มต้นในการดึงข้อมูล
        else:
            print("Error:", response.status_code)
            break
    print(f"requeste time use {time.time() - st}")

    # print(len(all_data))
    # with open('entity.json','w',encoding='utf8') as f:
    #     f.write(json.dumps(all_data,indent=4,ensure_ascii=False))



async def get_data():
    st = time.time()
    URL = f"https://ghoapi.azureedge.net/api/RSUD_490"
    page = 1000
    skip = 0
    data = []
    while True:
        query_row = f"?$top={page}&$skip={skip}"
        async with httpx.AsyncClient() as client:
            res = await client.get(URL + query_row)
            if res.status_code == 200:
                data.extend(res.json()['value'])
                if len(res.json()['value']) < page:
                    break
                else:
                    skip += page
            else:
                print(f"Error : {res.status_code}")
    print(f"requeste time use {time.time() - st}")
    # with open('entity.json','w',encoding='utf8') as f:
    #     f.write(json.dumps(data,indent=4,ensure_ascii=False))

async def get_data2():
    start = time.time()
    URL = f"https://ghoapi.azureedge.net/api/RSUD_490?$select=Id"
    async with httpx.AsyncClient() as client:
        res = await client.get(URL)
        if res.status_code == 200:
            pass
        else:
            print(f"Error : {res.status_code}")
    print(f"async requests time use {time.time() - start}")

def get_data3():
    start = time.time()
    URL = f"https://ghoapi.azureedge.net/api/RSUD_490?$select=Id"
    session = requests.Session()
    res = session.get(URL)
    if res.status_code == 200:
        pass
    else:
        print(f"Error : {res.status_code}")
    print(f"requeste time use {time.time() - start}")

if __name__ == '__main__':
    getodata()
    asyncio.run(get_data())
    # for i in range(1,21):
    #     print(f"Round {i}")
    #     get_data3()
    #     asyncio.run(get_data2())
    # getodata()
    # for i in range(1,11,2):
    #     x = 400000
    #     y = x // i**i
    #     print(y)
