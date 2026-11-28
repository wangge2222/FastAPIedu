#混合使用Path，Query和请求体参数
from fastapi import Body,FastAPI,Path,Query
from typing import Annotated
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None

class User(BaseModel):
    username:str
    full_name:str |None=None
@app.put("/items/{item_id}")
async def update_item(
    item_id:Annotated[int,Path(title="111",ge=0,le=1000)],
    importance:Annotated[int,Body()],
    q:str|None=None,
    item:Item|None=None,
    user:User|None=None

):
    results={"item_id":item_id,"item":item,"importance":importance,"q":q,"user":user}
    return results