from typing import Annotated
from  fastapi import FastAPI,Path,Query
app = FastAPI()
#你也可以使用 Path 为路径参数声明相同类型的校验和元数据。
"""@app.get("/items/{item_id}")
async def read_items(
        item_id:Annotated[int,Path(title="111")],
        q:Annotated[str|None,Query(alias="item-query")]=None
):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results"""
@app.get("/items/{item_id}")
async def read_item(
        item_id:Annotated[int,Path(title="111",ge=1)],q:str
):
    #ge: 大于等于greater than or equal
    #gt：大于
    #le：小于等于less than or equal
    #lt：小于

    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results
