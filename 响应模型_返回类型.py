#你可以通过为路径操作函数的返回类型添加注解来声明用于响应的类型。
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Item(BaseModel):
    name:str
    description:str
    price:float
    tax:float|None=None
    tags:list[str]=[]

@app.post("/items/",response_model=Item)
async def create_item(item:Item)->Item:
    return item

@app.get("/items/",response_model=list[Item])
async def read_items()->list[Item]:
    return [
        Item(name="Portal Gun",price=42.0),
        Item(name="Plumbus",price=32.0),
    ]



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("响应模型_返回类型:app", reload=True)