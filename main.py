from fastapi import FastAPI,Query
from enum import StrEnum
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None


class ModelName(StrEnum):
    alexnet="alexnet"
    resnet="resnet"
    lenet="lenet"
app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/models/{model_name}")
async def get(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name,"message":"Deep learning FTW!"}
    if model_name.value=="lenet":
        return {"model_name":model_name,"message":"Have some residuals"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")#从第0条开始，最多读取10条切片操作包左不包右
async def read_item(q:Annotated[str|None,Query(max_length=50)]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

@app.post("/items/")
async def creat_item(item:Item):
    item_dict=item.model_dump()
    if item.tax is not None:
        price_with_tax=item.price+item.tex
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict