# this is work with fast-api 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

# Connect MongoDB
client = MongoClient('mongodb+srv://admin:<password>@')
db = client['mydb'] # Create Database
collection = db['my_fast-api-collection'] # Create Collection

# Data Model
class MyModel(BaseModel):
    fname: str
    lname: str
    age: int

@app.get('/')
async def root():
    return {'message':'Hello world'}

# Create
@app.post('/create/')
async def create_data(mydb:MyModel):
    result = await collection.insert_one(mydb.dict())
    return {
        "id": str(result.inserted_id),
        "fname": mydb.fname,
        "lname":mydb.lname,
        "age":mydb.age
    }

# Read
@app.get('/read/{data_id}')
async def read_data(data_id:str):
    data = await collection.find_one({'_id': ObjectId(data_id)})
    # ---------------------------------- #
    if data:
        return{
            "id": str(data['_id']),
            "fname": data['fname'],
            "lname": data['lname'],
            "age": data['age']
        }
    else:
        raise HTTPException(status_code=404, detail="Data not found.")


# Put
@app.put('/put/{data_id}')
async def put_data(data_id: str, data:MyModel):
    result = await collection.update_one(
        {"_id": ObjectId(data_id)},{"$set": data.dict(exclude_unset=True)}
    )
    # ---------------------------------- #
    if result.modified_count == 1:
        return {"id": data_id, "fname":data.fname, "lname":data.lname, "age":data.age}
    else:
        return HTTPException(status_code=404, detail='Data not Found.')

# Delete
@app.delete('/delete/{data_id}')
async def delete_data(data_id:str):
    result = await collection.delete_one({"_id": ObjectId(data_id)})
    # ---------------------------------- #
    if result.deleted_count == 1:
        return {"status":"ok"}
    else:
        return HTTPException(status_code=404, detail='Data not Found.')
