import datetime
import json, psycopg2,requests,sqlalchemy
import pandas as pd
from sqlalchemy import text

url = 'https://ghoapi.azureedge.net/api/WHOSIS_000001?$select=Id,IndicatorCode,SpatialDimType,SpatialDim,TimeDimType'
url2 = 'https://ghoapi.azureedge.net/api/Dimension'
#
engine = sqlalchemy.create_engine(f"postgresql://postgres:nut.100240@localhost:5432/postgres")
#

with engine.connect() as conn:
    conn.execute(text('ALTER TABLE who_dimension_table ADD COLUMN key_id SERIAL PRIMARY KEY;'))
    conn.commit()

# data = []
# with requests.Session() as session:
#     res = session.get(url2)
#     columns = tuple(res.json()['value'][0].keys())
#     print(columns)
#     data.extend(res.json()['value'])
    # pd.read_json(json.dumps(res.json()['value']))\
    #     .to_sql('who_whosis_000001_table', engine, if_exists='append',index=False)

#
# pd.read_excel(r"C:\Users\ASUS\Downloads\opendata-rtddi-54-66-3month.xlsx")\
#     .to_sql('who_rtddi_table', engine, if_exists='append',index=False)

# with engine.connect() as conn:
    # conn.execute(text(
    #     f'''CREATE TABLE test_etl (
    #     {columns[0]} int primary key,
    #     {columns[1]} varchar,
    #     {columns[2]} varchar,
    #     {columns[3]} varchar,
    #     {columns[4]} varchar
    #     )'''
    # ))
    # conn.execute(
    #     text(
    #         f'''insert into test_etl (
    #         {columns[0]},
    #         {columns[1]},
    #         {columns[2]},
    #         {columns[3]},
    #         {columns[4]}
    #         ) values (
    #         :{columns[0]},
    #         :{columns[1]},
    #         :{columns[2]},
    #         :{columns[3]},
    #         :{columns[4]}
    #         )'''
    #     ),data
    #
    # )
    # conn.commit()

# with engine.connect() as conn:
#     # conn.execute(text(
#     #     f'''CREATE TABLE test_etl_who_dimension (
#     #     id serial primary key,
#     #     {columns[0]} varchar,
#     #     {columns[1]} varchar
#     #     )'''
#     # ))
#     conn.execute(
#         text(
#             f'''insert into test_etl_who_dimension (
#             {columns[0]},
#             {columns[1]}
#             ) values (
#             :{columns[0]},
#             :{columns[1]}
#             )'''
#         ),data)
#     conn.commit()