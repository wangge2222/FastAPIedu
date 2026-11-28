"""
使用 FastAPI，你可以定义、校验、
记录文档并使用任意深度嵌套的模型（归功于Pydantic）。
"""
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl
    #在 Image 模型中我们有一个 url 字段，我们可以把它声明为 Pydantic
    #的 HttpUrl，而不是 str
app=FastAPI()

class Image:
    url:HttpUrl#将被检查为是否有效的url
    name:str

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    tags:list[str]=[]#声明列表里的类型参数
    tags1:set[str]=set()
    image:list[Image]|None=None


@app.put("/item/{item_id}")
async def update_item(item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results